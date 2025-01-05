import numpy as np
import time
import torch

from pathlib import Path
import config


def print_epoch_info(enabled=True):
    """Decorator factory to optionally print epoch info"""

    def decorator(func):
        def wrapper(self, *args, **kwargs):
            epoch = args[0]
            train_index = kwargs.get("train_index")

            start_time = time.time()
            result = func(self, *args, **kwargs)
            epoch_time = time.time() - start_time

            if enabled:
                action_probs = self.model.action_probs[1:, :].squeeze()
                action_values = self.model.action_values.squeeze()

                # Get top 1 probabilities and their indices
                top_probs, top_indices = torch.topk(action_probs, 1)

                log_lines = [
                    f"Train_index: {train_index:>03d},    "
                    f"Epoch: {epoch:>03d},   Loss: {self.model.loss.item():>8.02f},   "
                    f"Time: {epoch_time:>5.2f}s",
                    "    Top 1 Action Probs and Values:",
                ]
                for idx, (prob, val_idx) in enumerate(
                    zip(top_probs, top_indices)
                ):
                    log_lines.append(
                        f"    {idx+1}: Prob={prob.item():.3f}, "
                        f"Value={action_values[val_idx].item():.3f}"
                    )

                # Print to console
                print("\n".join(log_lines))

                # Append to file
                results_path = Path("results/results.txt")
                with results_path.open("a") as f:
                    f.write(
                        "\n".join(log_lines) + "\n\n"
                    )  # Add extra newline for separation

            return result

        return wrapper

    return decorator


def print_train_info(enabled=True):
    """Decorator factory to optionally print training info"""

    def decorator(func):
        def wrapper(self, *args, **kwargs):
            topk = 3
            epoch = args[0]
            train_index = kwargs.get("train_index")

            if enabled:
                if train_index == 0 and epoch == 0:
                    wrapper.start_time = time.time()
                    # Create results directory if it doesn't exist
                    Path("results").mkdir(exist_ok=True)
                    # Save config to file
                    with open("results/results.txt", "w") as f:
                        f.write("=== CONFIG ===\n")
                        f.write(f"N_MODELS: {config.N_MODELS}\n")
                        f.write(f"EXP: {config.EXP}\n")
                        f.write(f"TRAIN: {config.TRAIN}\n")
                        f.write(f"ENV: {config.ENV}\n")
                        f.write(f"MODEL: {config.MODEL}\n")
                        f.write("\n=== TRAINING LOG ===\n")

            result = func(self, *args, **kwargs)

            if enabled:
                if epoch == self.train_config["n_epochs"] - 1:
                    retrain_time = time.time() - wrapper.start_time
                    action_probs = self.model.action_probs[1:, :].squeeze()
                    action_values = self.model.action_values.squeeze()
                    top_prob, top_idx = torch.topk(action_probs, topk)

                    log_lines = [
                        f"Train {train_index} completed in {retrain_time:.2f}s.",
                        "    Final top action probabilities and values:",
                    ]
                    for i, (idx, prob) in enumerate(zip(top_idx, top_prob)):
                        log_lines.append(
                            f"    {i+1}: Prob={prob.item():.3f}, Value={action_values[idx].item():.3f}"
                        )

                    # Print to console
                    print("\n".join(log_lines))

                    # Append to file
                    results_path = Path("results/results.txt")
                    with results_path.open("a") as f:
                        f.write(
                            "\n".join(log_lines) + "\n\n"
                        )  # Add extra newline for separation

            return result

        return wrapper

    return decorator


def normal_values_and_probs(len=100, mu=0, sigma=1, z_score=20):
    """Generate values and probabilities from a normal distribution.

    Args:
        len: Number of points to generate
        mu: Mean of the normal distribution
        sigma: Standard deviation of the normal distribution
        z_score: Number of standard deviations to extend in both directions

    Returns:
        tuple: (values, probabilities) where values are exponentiated
    """
    # Generate evenly spaced values between mu-z_score*sigma and mu+z_score*sigma
    values = np.linspace(mu - z_score * sigma, mu + z_score * sigma, len)

    # Calculate normal probabilities with given mu and sigma
    probs = np.exp(-0.5 * ((values - mu) / sigma) ** 2) / (
        sigma * np.sqrt(2 * np.pi)
    )

    # Normalize probabilities to sum to 1
    probs = probs / probs.sum()

    # Take exponential of values
    values = np.exp(values)

    return values.tolist(), probs.tolist()
