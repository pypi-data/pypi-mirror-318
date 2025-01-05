# import sys
# from icecream import ic
from typing import Dict, Any, List
from abc import ABC, abstractmethod

import torch
import torch.nn as nn
import torch.nn.functional as F


class Model(nn.Module, ABC):
    """Abstract base class for all models in the system.

    Inherits from torch.nn.Module and provides common interface for models.
    """

    def __init__(
        self, exp_config: Dict[str, Any], model_config: Dict[str, Any]
    ):
        """Initialize the model with configuration parameters.

        Args:
            exp_config: Experiment configuration dictionary
            model_config: Model-specific configuration dictionary
        """
        super().__init__()

        # Store configs as instance variables
        self.allow_short = exp_config["allow_short"]
        self.max_leverage = float(exp_config["max_leverage"])
        self.n_assets = exp_config["n_assets"]
        self.n_features = exp_config["n_features"]
        self.n_collections = exp_config["n_collections"]
        self.input_size = (self.n_assets, self.n_features, self.n_collections)
        self.initial_gumbel_temperature = model_config[
            "initial_gumbel_temperature"
        ]
        self.n_allowed_actions = model_config["n_allowed_actions"]
        self.memory_size = model_config["memory_size"]
        self.action_probs_size = (self.n_assets, self.n_allowed_actions)

        # Store action_probs, action_weights, action_values for outside access
        self.action_probs = torch.zeros(self.action_probs_size)
        self.action_weights = None
        self.action_values = None

    @abstractmethod
    def _calc_action_probs(self, x: torch.Tensor) -> torch.Tensor:
        """Compute the model's action given input tensor.

        Args:
            x: Input tensor of shape (n_assets, n_features, n_collections)

        Returns:
            Output tensor of shape (n_assets,) representing asset weights
        """
        pass

    @abstractmethod
    def get_trainable_params(self) -> List[torch.Tensor]:
        """Get list of trainable parameters.

        Returns:
            List of trainable parameter tensors
        """
        pass

    @abstractmethod
    def get_params_data(self) -> List[torch.Tensor]:
        """Get current parameter values.

        Returns:
            List of parameter value tensors
        """
        pass

    @abstractmethod
    def get_params_grad(self) -> List[torch.Tensor]:
        """Get current parameter gradients.

        Returns:
            List of parameter gradient tensors
        """
        pass

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Forward pass through the model.

        Args:
            x: Input tensor of shape (n_assets, n_features, n_collections)

        Returns:
            Output tensor of shape (n_assets,) containing sampled actions in [-max_leverage, max_leverage]
        """
        self._validate_input(x)
        probs = self._calc_action_probs(x)
        self._validate_probs(probs)
        self.action_probs = probs.detach()  # Store for outside access

        # Create action values based on max_leverage and allow_short
        if self.allow_short:
            self.action_values = torch.linspace(
                -self.max_leverage, self.max_leverage, self.n_allowed_actions
            )
        else:
            self.action_values = torch.linspace(
                0, self.max_leverage, self.n_allowed_actions
            )

        logits = torch.log(
            probs + 1e-8
        )  # Add small epsilon for numerical stability
        self.action_weights = self._gumbel_softmax(
            logits, tau=self.initial_gumbel_temperature, hard=True
        )

        # action_weights is (n_assets, n_allowed_actions) (continuous or one-hot)
        # action_values is (n_allowed_actions)
        # Use matrix multiplication to get weighted sum of action values
        actions = torch.matmul(self.action_weights, self.action_values)

        # Normalize actions to ensure they sum to max_leverage
        actions = self._normalize_actions(actions)
        self._validate_actions(actions)
        return actions

    def _validate_input(self, x: torch.Tensor) -> None:
        """Validate input tensor for forward pass.

        Args:
            x: Input tensor of shape (n_assets, n_features, n_collections)

        Raises:
            AssertionError: If input tensor shape or type is invalid
        """
        assert isinstance(x, torch.Tensor), (
            "Input must be a torch.Tensor but got type: " + str(type(x))
        )
        assert (
            x.dim() == 3
        ), f"Input tensor must be 3-dimensional but got {x.dim()} dimensions"
        assert (
            x.shape == self.input_size
        ), f"Input tensor shape must be {self.input_size} but got {x.shape}"

    def _gumbel_softmax(self, logits, tau=1.0, hard=True, dim=-1):
        """
        Sample from the Gumbel-Softmax distribution for multi-dimensional logits.

        Args:
            logits: Input logits (unnormalized log probabilities) of any shape.
            tau: Temperature parameter.
            hard: If True, return a one-hot vector (using argmax).
                Enable back-prop using straight-through estimator.
            dim: Dimension along which to apply the softmax operation.

        Returns:
            Sampled tensor (continuous or one-hot) of the same shape as logits.
        """
        # Sample Gumbel noise of the same shape as logits
        gumbel_noise = -torch.log(-torch.log(torch.rand_like(logits)))

        # Add Gumbel noise to logits
        y = logits + gumbel_noise

        # Apply softmax with temperature along the specified dimension
        y = F.softmax(y / tau, dim=dim)

        # If hard=True, use straight-through estimator
        if hard:
            # Create a one-hot vector from the argmax
            y_hard = torch.zeros_like(y)
            y_hard.scatter_(dim, torch.argmax(y, dim=dim, keepdim=True), 1.0)
            # Differentiable in backward pass
            y = (y_hard - y).detach() + y

        return y

    def _normalize_actions(
        self, actions_unnormalized: torch.Tensor
    ) -> torch.Tensor:
        """Normalize actions to ensure they sum to max_leverage.
        Weights for 0-th asset won't be trained.

        Args:
            actions_unnormalized: Unnormalized action tensor of shape (n_assets)

        Returns:
            Normalized action tensor of shape (n_assets)
        """
        if not self.allow_short:
            # Sum of positive actions (excluding the first one)
            positive_sum = actions_unnormalized[1:].sum()
            if positive_sum > self.max_leverage:
                # Scale down positive actions
                scale_factor = self.max_leverage / positive_sum
                actions_unnormalized[1:] *= scale_factor
            # Set first action to make total sum equal to max_leverage
            actions_unnormalized[0] = (
                self.max_leverage - actions_unnormalized[1:].sum()
            )
        else:
            # Sum of all actions (excluding the first one)
            other_sum = actions_unnormalized[1:].sum()
            if other_sum > 0:
                if other_sum > self.max_leverage:
                    # Scale down positive actions
                    scale_factor = self.max_leverage / other_sum
                    actions_unnormalized[1:] *= scale_factor
                # Set first action to make total sum equal to max_leverage
                actions_unnormalized[0] = (
                    self.max_leverage - actions_unnormalized[1:].sum()
                )
            else:
                if other_sum < -self.max_leverage:
                    # Scale up negative actions
                    scale_factor = -self.max_leverage / other_sum
                    actions_unnormalized[1:] *= scale_factor
                # Set first action to make total sum equal to max_leverage
                actions_unnormalized[0] = (
                    self.max_leverage - actions_unnormalized[1:].sum()
                )

        actions_normalized = actions_unnormalized
        return actions_normalized

    def _validate_actions(self, actions_normalized: torch.Tensor) -> None:
        """Validate that normalized actions meet constraints.

        Args:
            actions_normalized: Normalized action tensor of shape (n_assets,)

        Raises:
            AssertionError: If action constraints are violated
        """
        assert isinstance(actions_normalized, torch.Tensor), (
            "Actions must be a torch.Tensor but got type: "
            + str(type(actions_normalized))
        )
        assert (
            actions_normalized.dim() == 1
        ), f"Action tensor must be 1-dimensional but got {actions_normalized.dim()} dimensions"
        assert (
            actions_normalized.shape[0] == self.n_assets
        ), f"Action tensor must have {self.n_assets} elements but got {actions_normalized.shape[0]}"

        # Check sum of actions equals max_leverage
        assert torch.allclose(
            actions_normalized.sum(), torch.tensor(self.max_leverage)
        ), f"Sum of actions must equal {self.max_leverage} but got {actions_normalized.sum().item()}"

        if not self.allow_short:
            assert torch.all(
                actions_normalized >= 0.0
            ), f"All actions must be non-negative when shorting is not allowed but got min value {actions_normalized.min().item()}"

    def _validate_probs(self, probs: torch.Tensor) -> None:
        """Validate probability tensor from forward pass.

        Args:
            probs: Probability tensor of shape (n_assets, n_allowed_actions)

        Raises:
            AssertionError: If probability tensor shape or constraints are violated
        """
        assert isinstance(probs, torch.Tensor), (
            "Probs must be a torch.Tensor but got type: " + str(type(probs))
        )
        assert (
            probs.dim() == 2
        ), f"Probability tensor must be 2-dimensional but got {probs.dim()} dimensions"
        assert (
            probs.shape == self.action_probs_size
        ), f"Probability tensor shape must be {self.action_probs_size} but got {probs.shape}"

        if not self.allow_short:
            assert torch.all(
                probs >= 0.0
            ), f"All probability elements must be non-negative when shorting is not allowed but got min value {probs.min().item()}"

        # Check that each asset's probabilities sum to 1
        assert torch.allclose(
            probs.sum(dim=1), torch.ones(self.n_assets)
        ), f"Each asset's probabilities must sum to 1 but got sums: {probs.sum(dim=1)}"


class InputIndependentDistribution(Model, ABC):
    """Abstract base class for models that generate actions independent of input."""

    def __init__(
        self, exp_config: Dict[str, Any], model_config: Dict[str, Any]
    ):
        """Initialize the model with configuration parameters.

        Args:
            exp_config: Experiment configuration dictionary
            model_config: Model-specific configuration dictionary
        """
        super().__init__(exp_config, model_config)


class NaiveCategorical(InputIndependentDistribution):
    """Naive categorical distribution model that ignores input."""

    def __init__(
        self,
        exp_config: Dict[str, Any],
        model_config: Dict[str, Any],
        model_specific_config: Dict[str, Any],
    ):
        super().__init__(exp_config, model_config)
        # Initialize weights with uniform probabilities and require gradients
        self.weights = nn.Parameter(
            torch.ones(self.n_assets, self.n_allowed_actions)
        )

    def _calc_action_probs(self, x: torch.Tensor) -> torch.Tensor:
        """Compute action probabilities by applying softmax to weights.

        Args:
            x: Input tensor (ignored)

        Returns:
            Tensor of shape (n_assets, n_allowed_actions) with probabilities
        """
        return torch.softmax(self.weights, dim=1)

    def get_trainable_params(self) -> List[torch.Tensor]:
        """Get list of trainable parameters."""
        return [self.weights]

    def get_params_data(self) -> List[torch.Tensor]:
        """Get current parameter values."""
        return [self.weights.data]

    def get_params_grad(self) -> List[torch.Tensor]:
        """Get current parameter gradients."""
        return [self.weights.grad]
