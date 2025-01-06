from ..types.hf_models import HFChatModels

def litechat_model(model:HFChatModels):
    return model

def litellm_model(model:HFChatModels):
    return f"openai/{model}"