from config import EXP, TRAIN, ENV, MODEL, ENV_COLLECTIONS, MODEL_COLLECTIONS
from exp import Experiment


def main():
    best_actions = []
    model_count = 0

    for env_name, env_config in ENV_COLLECTIONS.items():
        for model_name, model_config in MODEL_COLLECTIONS.items():
            exp = Experiment(
                exp_config=EXP,
                train_config=TRAIN,
                env_config=ENV,
                model_config=MODEL,
                env_name=env_name,
                env_specific_config=env_config,
                model_name=model_name,
                model_specific_config=model_config,
                optimizer=TRAIN["optimizer"],
                lr=TRAIN["lr"],
            )

            result = exp.run()
            best_actions.append(result)
            print((env_name, model_name, result))
            model_count += 1

    print("All best actions:", best_actions)
    return sum(best_actions) / model_count


if __name__ == "__main__":
    average = main()
    print("Average of best actions:", average)
