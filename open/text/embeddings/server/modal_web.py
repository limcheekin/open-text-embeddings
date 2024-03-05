from open.text.embeddings.server.app import create_app
import modal
from modal import Stub, Volume, asgi_app

stub = Stub("open-text-embeddings")

volume = Volume.persisted("open-text-embeddings-volume")

@stub.function(
    image=modal.Image.from_registry("python:3.11.5-slim").pip_install(
        "starlette",
        "fastapi",
        "pydantic",
        "langchain",
        "torch",
        "transformers",
        "InstructorEmbedding",
        "sentence_transformers",
    ),
    volumes={"/root/.cache": volume},
    _allow_background_volume_commits=True,
)
@asgi_app()
def modal_app():
    """
    Run the modal app.
    """
    return create_app()
