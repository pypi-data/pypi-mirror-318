import asyncio
import json
import time
import uuid
import datetime
from contextlib import asynccontextmanager
from typing import Optional, Dict, Any, List, Union, AsyncGenerator

import uvicorn
from fastapi import FastAPI, HTTPException, Header, Request, WebSocket
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse

from litechat._core._oai import ChatHFClient
from fastapi.responses import StreamingResponse

hf_client: Union[ChatHFClient, None] = None
_animation = None
from litechat.types.hf_models import HFChatModels, AVAILABLE_MODELS


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    global hf_client, _animation
    hf_client = await ChatHFClient.create(_animation == False)
    yield
    # Shutdown
    if hf_client:
        await hf_client.close()


app = FastAPI(title="OpenAI Compatible API", lifespan=lifespan)


# Models for request/response validation
class ChatMessage(BaseModel):
    role: str
    content: str


class ChatCompletionRequest(BaseModel):
    model: HFChatModels
    messages: List[ChatMessage]
    stream: Optional[bool] = False
    temperature: Optional[float] = 1.0
    max_tokens: Optional[int] = None
    conv_id: Optional[str] = None
    web_search: Optional[bool] = False


class ImageGenerationRequest(BaseModel):
    prompt: str
    model: Optional[str] = "dall-e-2"
    n: Optional[int] = 1
    size: Optional[str] = "1024x1024"


class EmbeddingRequest(BaseModel):
    input: str
    model: Optional[str] = "text-embedding-ada-002"


class ModerationRequest(BaseModel):
    input: str
    model: Optional[str] = "text-moderation-latest"


async def generate_chunks(messages: List[Dict[str, str]],
                          conversation_id=None,
                          web_search=None,
                          model: HFChatModels = None
                          ) -> AsyncGenerator[str, None]:
    """Async generator for streaming responses"""
    completion = await hf_client.completions.create(
        model=model,
        messages=messages,
        stream=True,
        web_search=web_search,
        conversation_id=conversation_id or str(uuid.uuid4())
    )

    async for chunk in completion:
        yield chunk.model_dump_json() + "\n"


@app.post("/v1/chat/completions")
async def create_chat_completion(request: ChatCompletionRequest):
    if request.stream:
        return StreamingResponse(
            generate_chunks([{"role": m.role, "content": m.content} for m in request.messages],
                            conversation_id=request.conv_id or str(uuid.uuid4()),
                            web_search=request.web_search,
                            model=request.model),
            media_type="application/x-ndjson"
        )

    # Non-streaming response
    conversation_id = request.conv_id or str(uuid.uuid4())
    response = await hf_client.completions.create(
        model=request.model,
        messages=[{"role": m.role, "content": m.content} for m in request.messages],
        stream=False,
        web_search=request.web_search,
        conversation_id=conversation_id
    )
    return response.model_dump()


# Image generation endpoint
@app.post("/v1/images/generations")
async def create_image(
    request: ImageGenerationRequest
):
    response = {
        "created": int(datetime.datetime.now().timestamp()),
        "data": [
            {
                "url": f"https://dummy-image-{i}.jpg",
                "b64_json": None
            }
            for i in range(request.n)
        ]
    }
    return response


# Embeddings endpoint
@app.post("/v1/embeddings")
async def create_embedding(
    request: EmbeddingRequest
):
    # Generate dummy embedding vector
    dummy_embedding = [0.1] * 1536  # OpenAI's ada-002 uses 1536 dimensions

    response = {
        "object": "list",
        "data": [
            {
                "object": "embedding",
                "embedding": dummy_embedding,
                "index": 0
            }
        ],
        "model": request.model,
        "usage": {
            "prompt_tokens": len(request.input.split()),
            "total_tokens": len(request.input.split())
        }
    }
    return response


# Moderations endpoint
@app.post("/v1/moderations")
async def create_moderation(
    request: ModerationRequest
):
    response = {
        "id": f"modr-{uuid.uuid4()}",
        "model": request.model,
        "results": [
            {
                "flagged": False,
                "categories": {
                    "sexual": False,
                    "hate": False,
                    "harassment": False,
                    "self-harm": False,
                    "sexual/minors": False,
                    "hate/threatening": False,
                    "violence/graphic": False,
                    "self-harm/intent": False,
                    "self-harm/instructions": False,
                    "harassment/threatening": False,
                    "violence": False
                },
                "category_scores": {
                    "sexual": 0.0,
                    "hate": 0.0,
                    "harassment": 0.0,
                    "self-harm": 0.0,
                    "sexual/minors": 0.0,
                    "hate/threatening": 0.0,
                    "violence/graphic": 0.0,
                    "self-harm/intent": 0.0,
                    "self-harm/instructions": 0.0,
                    "harassment/threatening": 0.0,
                    "violence": 0.0
                }
            }
        ]
    }
    return response


# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.get("/api/tags")
async def list_models():
    """List available models"""
    def get_json(model):
        return {
            "name": model,
            "modified_at": str(time.time()),
            "size": 32,
            "digest": "dummy",
            "details": {
                "family": "unk",
                "parameter_size": "unk"
            }
        }
    models = [get_json(model) for model in AVAILABLE_MODELS]
    return {"models": models}

class StateUpdateRequest(BaseModel):
    model:Optional[str] = None
    system_prompt:Optional[str] = None
    web_search:Optional[bool] = None

@app.post("/litechat/update-state")
async def state_update(request:StateUpdateRequest):
    if request.model is not None:
        await hf_client.hf.set_model(request.model)
    if request.system_prompt is not None:
        await hf_client.hf.set_system_prompt(request.system_prompt)
    if request.web_search is not None:
        await hf_client.hf.set_web_search(request.web_search)
    res = {
        "system_prompt": hf_client.hf.system_prompt,
        "web_search": hf_client.hf.web_search,
        "model": hf_client.hf.model
    }
    return JSONResponse(status_code=200,content=res)


@app.post("/litechat/get-state")
async def state_update():
    return {
        "system_prompt": hf_client.hf.system_prompt,
        "web_search": hf_client.hf.web_search,
        "model": hf_client.hf.model
    }


def litechat_server(host="0.0.0.0", port=8000, log_level="info", animation=False):
    global _animation
    _animation = animation
    uvicorn.run(app, host=host, port=port, log_level=log_level)

if __name__ == '__main__':
    litechat_server(host="0.0.0.0", animation=True)
