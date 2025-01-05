import sys  # noqa: F401
from icecream import ic  # noqa: F401
from itertools import product

import torch
import torch.optim as optim

from env import IID, Markov
from model import NaiveCategorical
from utils import print_epoch_info, print_train_info


class Experiment:
    """Experiment class to manage and run an experiment"""

    def __init__(
        self,
        exp_config: dict,
        train_config: dict,
        env_config: dict,
        model_config: dict,
        env_name: str,
        env_specific_config: dict,
        model_name: str,
        model_specific_config: dict,
        optimizer,
        lr,
    ):
        self.exp_config = exp_config
        self.train_config = train_config
        self.env_config = env_config
        self.model_config = model_config
        self.env_name = env_name
        self.env_specific_config = env_specific_config
        self.model_name = model_name
        self.model_specific_config = model_specific_config

        # Initialize environment and model based on configurations
        self.env = self._init_environment()
        self.model = self._init_model()

        torch.set_printoptions(precision=3)

        if optimizer == "Adam":
            self.optimizer = optim.Adam(
                self.model.get_trainable_params(), lr=lr
            )

    def _init_environment(self):
        """Initialize environment based on configuration"""
        exp_config = self.exp_config
        env_config = self.env_config
        env_specific_config = self.env_specific_config

        if self.env_specific_config["env_type"] == "iid":
            return IID(exp_config, env_config, env_specific_config)
        elif self.env_specific_config["env_type"] == "markov":
            return Markov(exp_config, env_config, env_specific_config)
        else:
            raise ValueError(
                f"Unknown env_type: {self.env_specific_config['env_type']}"
            )

    def _init_model(self):
        """Initialize model based on configuration"""
        exp_config = self.exp_config
        model_config = self.model_config
        model_specific_config = self.model_specific_config

        if self.model_specific_config["model_type"] == "NaiveCategorical":
            return NaiveCategorical(
                exp_config, model_config, model_specific_config
            )
        else:
            raise ValueError(
                f"Unknown model_type: {self.model_specific_config['model_type']}"
            )

    def episode_reward(
        self, epoch: int, episode: int, print_actions: bool = False
    ) -> torch.tensor:
        episode_r = torch.tensor(0.0)
        state = self.env.get_next_state()
        if epoch == 0 and episode == 0:
            # print("------------ Start of Episode:  ", episode, "------------")
            for round in range(self.exp_config["n_rounds"]):
                action = self.model(state)
                # if print_actions:
                #     print(
                #         f"Action at round {round}:  ",
                #         action.data,
                #     )
                next_state, env_reward = self.env.next(action)
                # Subtract transaction fee based on action magnitude
                # Convert transaction fee to log space: log(1 - fee * |action|)
                # Multiply by 2 to account for both opening and closing positions
                transaction_cost = torch.log1p(
                    -2
                    * self.train_config["transaction_fee"]
                    * torch.sum(torch.abs(action[1:]))
                )
                episode_r += env_reward + transaction_cost
                # ic(env_reward.data)
                state = next_state
            # sys.exit()
            self.env.reset()
            # print("------------- End of Episode:  ", episode, "-------------")
        else:
            for round in range(self.exp_config["n_rounds"]):
                action = self.model(state)
                # if print_actions:
                #     print(
                #         f"Action at round {round}:  ",
                #         action.data,
                #     )
                next_state, env_reward = self.env.next_replay(action)
                # Subtract transaction fee based on action magnitude
                # Convert transaction fee to log space: log(1 - fee * |action|)
                # Multiply by 2 to account for both opening and closing positions
                transaction_cost = torch.log1p(
                    -2
                    * self.train_config["transaction_fee"]
                    * torch.sum(torch.abs(action[1:]))
                )
                episode_r += env_reward + transaction_cost
                state = next_state
            self.env.reset_replay()

        return episode_r

    def epoch_reward(self, epoch: int) -> torch.tensor:
        epoch_r = torch.tensor(0.0)
        for episode in range(self.train_config["n_episodes"]):
            episode_r = self.episode_reward(epoch, episode, print_actions=True)
            epoch_r += episode_r
        return epoch_r / self.train_config["n_episodes"]

    @print_train_info(enabled=True)
    @print_epoch_info(enabled=False)
    def update_model(self, epoch: int, train_index: int = None):
        self.optimizer.zero_grad()
        loss = -self.epoch_reward(epoch)
        loss.backward()
        self.optimizer.step()

    def run(self):
        """Run the experiment"""
        n_trains = self.exp_config["n_trains"]
        n_epochs = self.train_config["n_epochs"]

        for train_index, epoch in product(range(n_trains), range(n_epochs)):
            self.update_model(epoch, train_index=train_index)

        # Return final top action value
        action_probs = self.model.action_probs[1:, :].squeeze()
        action_values = self.model.action_values.squeeze()
        top_prob, top_idx = torch.topk(action_probs, 1)
        return action_values[top_idx].item()
