# Modal Lab web app for open-text-embeddings.
from modal import Image, Stub, asgi_app

stub = Stub(os.environ["STUB"])

image = Image.from_dockerfile(
    "Dockerfile-Modal", force_build=True
).env({
    "MODEL": os.environ["MODEL"],
    "NORMALIZE_EMBEDDINGS": os.environ["NORMALIZE_EMBEDDINGS"],
    "VERBOSE": os.environ["VERBOSE"],
    "HF_HOME": "/tmp/hf_home",
})

cpu = float(os.getenv("CPU", 2.0))
memory = int(os.getenv("MEMORY"), 2048) 
timeout = int(os.getenv("TIMEOUT"), 600)
keep_warm = int(os.getenv("KEEP_WARM"), 1)
@stub.function(image=image, cpu=cpu, memory=memory, timeout=timeout, keep_warm=keep_warm)
@asgi_app()
def fastapi_app():
    from open.text.embeddings.server.app import create_app
    import os
    print("os.cpu_count()", os.cpu_count())
    app = create_app()
    return app


if __name__ == "__main__":
    stub.deploy("webapp")
