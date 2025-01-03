
import yaml
from typing import Type

from hwhkit.llm.models.base import LanguageModelFactory, LanguageModelProperty, LanguageModel
from hwhkit.llm.models.gpt import GPTStrategy


def load_models_from_config(
        config_file: str='llm_config.yaml', keys_file: str = "llm_key.yaml"
) -> Type[LanguageModelFactory]:

    with open(config_file, "r") as f:
        config = yaml.safe_load(f)

    with open(keys_file, "r") as f:
        keys = yaml.safe_load(f).get("keys", {})

    models_config = config.get("models", {})
    for name, model_config in models_config.items():
        model_keys = {}
        for key_config in model_config.get("keys", []):
            key_name = key_config["name"]
            if key_name in keys:
                model_keys[key_name] = keys[key_name]

        model = None
        if name.startswith("gpt"):
            strategy = GPTStrategy(keys=model_keys, model_property=LanguageModelProperty(**model_config))
            model = LanguageModel(strategy)

        if model:
            LanguageModelFactory.register_model_instance(name, model)
    return LanguageModelFactory