# Modal Lab web app for open-text-embeddings.
from modal import Image, App, asgi_app
import os

app = App(os.environ["APP_NAME"])

image = Image.from_registry("python:3.11-slim-bookworm"
        ).copy_local_file(f"{os.environ['HOME']}/download.sh"
        ).dockerfile_commands(
            "RUN apt-get update && apt-get install -y git-lfs",
            f"RUN chmod +x *.sh && ./download.sh {os.environ['MODEL']}"
        ).pip_install("open-text-embeddings[server]", "langchain_community"
        ).env({
            "MODEL": os.environ["MODEL"],
            "NORMALIZE_EMBEDDINGS": os.environ["NORMALIZE_EMBEDDINGS"],
            "VERBOSE": os.environ["VERBOSE"],
            "HF_HOME": "/tmp/hf_home",
            "APP_NAME": os.environ["APP_NAME"],
        })


cpu = float(os.getenv("CPU", 2.0))
memory = int(os.getenv("MEMORY", 2048)) 
timeout = int(os.getenv("TIMEOUT", 600))
keep_warm = int(os.getenv("KEEP_WARM", 1))
@app.function(image=image, cpu=cpu, memory=memory, timeout=timeout, keep_warm=keep_warm)
@asgi_app()
def fastapi_app():
    from open.text.embeddings.server.app import create_app
    import os
    print("os.cpu_count()", os.cpu_count())
    return create_app()


if __name__ == "__main__":
    app.deploy("webapp")
