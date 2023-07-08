
from typing import List, Optional, Union
from starlette.concurrency import run_in_threadpool
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from langchain.embeddings import HuggingFaceEmbeddings
import os

router = APIRouter()


def create_app():
    app = FastAPI(
        title="Open Text Embeddings API",
        version="0.0.1",
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(router)

    return app


class CreateEmbeddingRequest(BaseModel):
    model: Optional[str] = Field(
        description="The model to use for generating embeddings.")
    input: Union[str, List[str]] = Field(description="The input to embed.")
    user: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "input": "The food was delicious and the waiter...",
            }
        }


class Embedding(BaseModel):
    embedding: List[float]


class CreateEmbeddingResponse(BaseModel):
    data: List[Embedding]


embeddings = None


def _create_embedding(
    request: CreateEmbeddingRequest
):
    global embeddings

    if embeddings is None:
        model_name = request.model or os.environ["MODEL"]
        print("Loading model:", model_name)
        embeddings = HuggingFaceEmbeddings(model_name=model_name)

    if isinstance(request.input, str):
        return CreateEmbeddingResponse(data=[Embedding(embedding=embeddings.embed_query(request.input))])
    else:
        data = [Embedding(embedding=embedding)
                for embedding in embeddings.embed_documents(request.input)]
        return CreateEmbeddingResponse(data=data)


@router.post(
    "/v1/embeddings",
    response_model=CreateEmbeddingResponse,
)
async def create_embedding(
    request: CreateEmbeddingRequest
):
    return await run_in_threadpool(
        _create_embedding(request)
    )
