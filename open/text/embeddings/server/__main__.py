"""FastAPI server for open-text-embeddings.

To run this example:

```bash
pip install -r --no-cache-dir server-requirements.txt
pip install --no-cache-dir uvicorn
```

Then run:
```
MODEL=intfloat/e5-large-v2 python -m open.text.embeddings.server
```

Then visit http://localhost:8000/docs to see the interactive API docs.

"""
import uvicorn
import os
from open.text.embeddings.server.app import create_app

if __name__ == "__main__":
    app = create_app()

    uvicorn.run(
        app, host=os.getenv("HOST", "localhost"), port=int(os.getenv("PORT", 8000))
    )
