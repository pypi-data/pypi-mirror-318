"""Centralized configuration for all experiments.

This module contains all configuration parameters for the application,
including experiment settings, environment configurations, and model parameters.
"""

import utils

N_MODELS = 50

EXP = {
    # used by both env.py and model.py
    "allow_short": False,
    "max_leverage": 1,
    "n_assets": 2,
    "n_features": 1,
    "n_collections": 1,
    "n_trains": 50,
    "n_rounds": 10,
}

TRAIN = {
    "n_epochs": 3,
    "n_episodes": 3,
    "entropy_regularized": False,
    "optimizer": "Adam",  # "Adam" or "SGD"
    "lr": 0.05,
    "transaction_fee": 1e-3
}

ENV = {}

MODEL = {
    "initial_gumbel_temperature": 5,
    "n_allowed_actions": 51,
    "memory_size": 64,
}


values, probs = utils.normal_values_and_probs(
    len=100, mu=0, sigma=0.03, z_score=20
)

ENV_COLLECTIONS = {
    "iid_normal": {
        "env_type": "iid",
        "state_transition_params": {
            "values": values,
            "probs": probs,
        },
    },
    # "iid_stable_uniform": {
    #     "env_type": "iid",
    #     "state_transition_params": {
    #         "values": [1.5, 1.0, 0.6667],
    #         "probs": [0.3333, 0.3334, 0.333],
    #     },
    # },
    # "iid_stable_valley": {
    #     "env_type": "iid",
    #     "state_transition_params": {
    #         "values": [1.5, 1.0, 0.6667],
    #         "probs": [0.5, 0.0, 0.5],
    #     },
    # },
    # "iid_stable_hill": {
    #     "env_type": "iid",
    #     "state_transition_params": {
    #         "values": [1.5, 1.0, 0.6667],
    #         "probs": [0.05, 0.9, 0.05],
    #     },
    # },
}

MODEL_COLLECTIONS = {
    **{
        f"NaiveCategorical{i}": {"model_type": "NaiveCategorical"}
        for i in range(1, N_MODELS + 1)
    },
    # "constant_2": {
    #     "model_type": "constant",
    # },
    # "markov": {},
    # "mlp": {},
}
