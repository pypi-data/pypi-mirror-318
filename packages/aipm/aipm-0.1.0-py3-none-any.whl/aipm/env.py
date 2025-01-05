# import sys
# from icecream import ic
import torch
import pickle
import os
from typing import Tuple, Optional
from abc import ABC, abstractmethod


class Env(ABC):
    """Abstract base class for all environments"""

    def __init__(
        self,
        exp_config: dict,
        env_config: dict,
    ) -> None:
        self.allow_short = exp_config["allow_short"]
        self.max_leverage = float(exp_config["max_leverage"])
        self.n_assets = exp_config["n_assets"]
        self.n_features = exp_config["n_features"]
        self.n_collections = exp_config["n_collections"]
        self.n_trains = exp_config["n_trains"]
        self.n_rounds = exp_config["n_rounds"]
        self.state_size = (self.n_assets, self.n_features, self.n_collections)

        self.train_index: int = 0
        self.round: int = 0
        self.replay_round: int = 0
        self.state: Optional[torch.Tensor] = (
            None  # Tensor of shape (n_assets, n_features, n_collections)
        )
        # where the 0-th feature must be log(price[t]/price[t-1])

    def next(self, action: torch.Tensor) -> Tuple[torch.Tensor, float]:
        """Process action and return next state and reward
        Args:
            action: torch.Tensor of shape (n_assets,)
        Returns:
            Tuple of (next_state, reward) where:
                next_state: torch.Tensor of shape (n_assets, n_features, n_collections)
                reward: float = log(I[t]/I[t-1])
        Raises:
            RuntimeError: If train_index >= n_trains or round >= n_rounds
        """
        assert (
            self.train_index < self.n_trains
        ), f"train_index {self.train_index} >= n_trains {self.n_trains}"
        assert (
            self.round < self.n_rounds
        ), f"round {self.round} >= n_rounds {self.n_rounds}. Please call reset()."

        self.validate_input(action)
        next_state = self.get_next_state()
        self.validate_next_state(next_state)
        reward = self.get_reward(action, next_state)
        self.round += 1
        return next_state, reward

    def next_replay(
        self, action: torch.Tensor, replay_mode: str = "last"
    ) -> Tuple[torch.Tensor, float]:
        """Process action in replay mode and return next state and reward
        Args:
            action: torch.Tensor of shape (n_assets,)
            replay_mode: str = "last" or "specific" (default: "last")
        Returns:
            Tuple of (next_state, reward) where:
                next_state: torch.Tensor of shape (n_assets, n_features, n_collections)
                reward: float = log(I[t]/I[t-1])
        Raises:
            RuntimeError: If replay_round >= n_rounds
        """
        assert (
            self.train_index >= 1
        ), "Cannot replay without previous training data (train_index must be >= 1)"
        assert (
            self.replay_round < self.n_rounds
        ), f"replay_round {self.replay_round} >= n_rounds {self.n_rounds}. Please call reset_replay()."

        self.validate_input(action)
        next_state = self.get_next_replay_state(replay_mode)
        self.validate_next_state(next_state)
        reward = self.get_reward(action, next_state)
        self.replay_round += 1
        return next_state, reward

    @abstractmethod
    def get_next_replay_state(self, replay_mode: str = "last") -> torch.Tensor:
        """Calculate and return next state for given action
        Args:
            replay_mode: str = "last" or "specific" (default: "last")
        Returns:
            torch.Tensor of shape (n_assets, n_features, n_collections)
        """
        pass

    def get_reward(
        self, action: torch.Tensor, next_state: torch.Tensor
    ) -> float:
        """Calculate and return reward for given action
        Return = log(I[t]/I[t-1])
        Args:
            action: torch.Tensor of shape (n_assets,)
            next_state: torch.Tensor of shape (n_assets, n_features, n_collections)
        Returns:
            float
        """
        price_relatives = self.get_price_relative(next_state)

        # Compute dot product and take log
        portfolio_return = torch.dot(action, price_relatives)
        portfolio_return = torch.log(portfolio_return)
        return portfolio_return

    def reset(self) -> None:
        """Reset environment state"""
        self.train_index += 1
        self.round = 0
        self.state = None

    def reset_replay(self) -> None:
        """Reset replay state"""
        self.replay_round = 0

    def get_price_relative(self, next_state: torch.Tensor) -> torch.Tensor:
        """Calculate price relative using the 0-th feature
        Args:
            next_state: torch.Tensor of shape (n_assets, n_features, n_collections)
        Returns:
            torch.Tensor of shape (n_assets,) containing price relatives
        """
        # Extract 0-th feature and sum across collections
        price_relative = next_state[:, 0, :].sum(dim=1)
        # Apply exponential function
        return torch.exp(price_relative)

    def validate_input(self, action: torch.Tensor) -> None:
        """Validate action tensor for next() method.

        Args:
            action: Action tensor of shape (n_assets,)

        Raises:
            AssertionError: If validation fails
        """
        assert isinstance(
            action, torch.Tensor
        ), "Action must be a torch.Tensor"
        assert action.dim() == 1, "Action tensor must be 1-dimensional"
        assert (
            action.size(0) == self.n_assets
        ), f"Action tensor size must be {self.n_assets}"

        if not self.allow_short:
            assert torch.all(
                action >= 0.0
            ), "All action elements must be non-negative when shorting is not allowed"

        assert torch.isclose(
            action.sum(), torch.tensor(self.max_leverage), atol=1e-5
        ), f"Sum of action elements must be max leverage: {self.max_leverage}"

    def validate_next_state(self, next_state: torch.Tensor) -> None:
        """Validate next_state tensor for next() method.

        Args:
            next_state: Next state tensor of shape (n_assets, n_features, n_collections)

        Raises:
            AssertionError: If validation fails
        """
        assert isinstance(
            next_state, torch.Tensor
        ), "Next state must be a torch.Tensor"
        assert next_state.dim() == 3, "Next state tensor must be 3-dimensional"
        assert (
            next_state.shape == self.state_size
        ), f"Next state tensor shape must be {self.state_size}"


class Sim(Env):
    """Base class for simulated environments"""

    def __init__(
        self,
        exp_config: dict,
        env_config: dict,
    ) -> None:
        super().__init__(exp_config, env_config)
        self.saved_states = {}  # Dictionary to store states with (train_index, round) keys

    def next(self, action: torch.Tensor) -> Tuple[torch.Tensor, float]:
        """Process action and return next state and reward
        Args:
            action: torch.Tensor of shape (n_assets,)
        Returns:
            Tuple of (next_state, reward) where:
                next_state: torch.Tensor of shape (n_assets, n_features, n_collections)
                reward: float = log(I[t]/I[t-1])
        """
        next_state, reward = super().next(action)
        # starting index (0, 0)
        self.saved_states[(self.train_index, self.round - 1)] = (
            next_state.clone()
        )

        # Save to pickle file when reaching final round
        if self.round == self.n_rounds:
            # Create directory if it doesn't exist
            os.makedirs("data/sim/iid", exist_ok=True)
            filename = f"data/sim/iid/replay_{self.train_index}.pkl"
            with open(filename, "wb") as f:
                pickle.dump(self.saved_states, f)
            # print(f"Saved replay states to {filename}")
        return next_state, reward


class Real(Env):
    """Class for real-world environments"""

    def __init__(
        self,
        exp_config: dict,
        env_config: dict,
    ) -> None:
        super().__init__(exp_config, env_config)


class IID(Sim):
    """IID simulated environment"""

    def __init__(
        self,
        exp_config: dict,
        env_config: dict,
        env_specific_config: dict,
    ) -> None:
        super().__init__(exp_config, env_config)
        self.state_transition_params = env_specific_config[
            "state_transition_params"
        ]

    def get_next_state(self) -> torch.Tensor:
        """Calculate next state based on IID process
        Returns:
            torch.Tensor of shape (n_assets, n_features, n_collections)
        """
        # Get parameters from config
        values = torch.tensor(self.state_transition_params["values"])
        probs = torch.tensor(self.state_transition_params["probs"])

        # Sample values according to probabilities
        sampled_indices = torch.multinomial(
            probs,
            self.n_assets * self.n_features * self.n_collections,
            replacement=True,
        )
        sampled_values = values[sampled_indices]

        # Reshape to match state dimensions and take log
        next_state = sampled_values.reshape(self.state_size)

        # Set 0-th asset values to 1
        next_state[0, :, :] = 1.0

        return torch.log(next_state)

    def get_next_replay_state(self, replay_mode: str = "last") -> torch.Tensor:
        """Calculate and return next state for replay mode
        Args:
            replay_mode: str = "last" or "specific" (default: "last")
        Returns:
            torch.Tensor of shape (n_assets, n_features, n_collections)
        """
        if replay_mode == "last":
            # Load saved states from previous training run
            filename = f"data/sim/iid/replay_{self.train_index-1}.pkl"
            with open(filename, "rb") as f:
                saved_states = pickle.load(f)

            # Get the state for the current replay round
            next_replay = saved_states[
                (self.train_index - 1, self.replay_round)
            ]
            return next_replay


class Markov(Sim):
    """Markov simulated environment"""

    def __init__(
        self,
        exp_config: dict,
        env_config: dict,
        env_specific_config: dict,
    ) -> None:
        super().__init__(exp_config, env_config)
        self.state_transition_params = env_specific_config[
            "state_transition_params"
        ]
        self.reward_params = env_specific_config["reward_params"]

    def get_next_state(self) -> torch.Tensor:
        """Calculate next state based on Markov process
        Returns:
            torch.Tensor of shape (n_assets, n_features, n_collections)
        """
        # Implement Markov-specific state transition
        pass
