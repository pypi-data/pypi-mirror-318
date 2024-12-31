import os
from logging import Logger

import requests
from openai import OpenAI
from openai.lib.azure import AzureOpenAI
from pymultirole_plugins.util import comma_separated_to_list
from strenum import StrEnum

logger = Logger("pymultirole")
DEFAULT_CHAT_GPT_MODEL = "gpt-4o-mini"


# Now use default retry with backoff of openai api
def openai_chat_completion(prefix, base_url, **kwargs):
    client = set_openai(prefix, base_url)
    response = client.chat.completions.create(**kwargs)
    return response


def openai_list_models(prefix, base_url, **kwargs):
    def sort_by_created(x):
        if 'created' in x:
            return x['created']
        elif 'created_at' in x:
            return x['created_at']
        elif 'deprecated' in x:
            return x['deprecated'] or 9999999999
        else:
            return x.id

    models = []
    client = set_openai(prefix, base_url)
    if prefix.startswith("DEEPINFRA"):
        deepinfra_url = client.base_url
        deepinfra_models = {}
        public_models_list_url = f"{deepinfra_url.scheme}://{deepinfra_url.host}/models/list"
        response = requests.get(public_models_list_url,
                                headers={'Accept': "application/json", 'Authorization': f"Bearer {client.api_key}"})
        if response.ok:
            resp = response.json()
            mods = sorted(resp, key=sort_by_created, reverse=True)
            mods = list(
                {m['model_name'] for m in mods if m['type'] == 'text-generation'})
            deepinfra_models.update({m: m for m in mods})

        private_models_list_url = f"{deepinfra_url.scheme}://{deepinfra_url.host}/models/private/list"
        response = requests.get(private_models_list_url,
                                headers={'Accept': "application/json", 'Authorization': f"Bearer {client.api_key}"})
        if response.ok:
            resp = response.json()
            mods = sorted(resp, key=sort_by_created, reverse=True)
            mods = list(
                {m['model_name'] for m in mods if m['type'] == 'text-generation'})
            deepinfra_models.update({m: m for m in mods})

        deployed_models_list_url = f"{deepinfra_url.scheme}://{deepinfra_url.host}/deploy/list/"
        response = requests.get(deployed_models_list_url,
                                headers={'Accept': "application/json", 'Authorization': f"Bearer {client.api_key}"})
        if response.ok:
            resp = response.json()
            mods = sorted(resp, key=sort_by_created, reverse=True)
            mods = list(
                {m['model_name'] for m in mods if m['task'] == 'text-generation' and m['status'] == 'running'})
            deepinfra_models.update({m: m for m in mods})
        models = list(deepinfra_models.keys())
    elif prefix.startswith("AZURE"):
        models = comma_separated_to_list(os.getenv(prefix + "OPENAI_DEPLOYMENT_ID", None))
    else:
        response = client.models.list(**kwargs)
        models = sorted(response.data, key=sort_by_created, reverse=True)
        models = [m.id for m in models]
    return models


def set_openai(prefix, base_url):
    if prefix.startswith("AZURE"):
        client = AzureOpenAI(
            # This is the default and can be omitted
            api_key=os.getenv(prefix + "OPENAI_API_KEY"),
            azure_endpoint=base_url,
            api_version=os.getenv(prefix + "OPENAI_API_VERSION", None),
            # azure_deployment=os.getenv(prefix + "OPENAI_DEPLOYMENT_ID", None)
        )
    else:
        client = OpenAI(
            # This is the default and can be omitted
            api_key=os.getenv(prefix + "OPENAI_API_KEY"),
            base_url=base_url
        )
    return client


def gpt_filter(m: str):
    return m.startswith('gpt') and not m.startswith('gpt-3.5-turbo-instruct') and 'vision' not in m


NO_DEPLOYED_MODELS = 'no deployed models - check API key'


# @lru_cache(maxsize=None)
def create_openai_model_enum(name, prefix="", base_url=None, key=lambda m: m):
    chat_gpt_models = []
    default_chat_gpt_model = None
    try:
        chat_gpt_models = [m for m in openai_list_models(prefix, base_url) if key(m)]
        if chat_gpt_models:
            default_chat_gpt_model = DEFAULT_CHAT_GPT_MODEL if DEFAULT_CHAT_GPT_MODEL in chat_gpt_models else \
                chat_gpt_models[0]
    except BaseException:
        logger.warning("Can't list models from endpoint", exc_info=True)

    if len(chat_gpt_models) == 0:
        chat_gpt_models = [NO_DEPLOYED_MODELS]
    models = [("".join([c if c.isalnum() else "_" for c in m]), m) for m in chat_gpt_models]
    model_enum = StrEnum(name, dict(models))
    default_chat_gpt_model = model_enum(default_chat_gpt_model) if default_chat_gpt_model is not None else None
    return model_enum, default_chat_gpt_model
