from setuptools import setup

from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="open_text_embeddings",
    url="https://github.com/limcheekin/open-text-embeddings",
    description="Open Source Text Embedding Models with OpenAI API-Compatible Endpoint",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="1.0.2",
    author="Lim Chee Kin",
    author_email="limcheekin@vobject.com",
    license="MIT",
    package_dir={"open.text.embeddings": "open/text/embeddings",
                 "open.text.embeddings.server": "open/text/embeddings/server"},
    packages=["open.text.embeddings", "open.text.embeddings.server"],
    install_requires=["langchain>=0.0.200"],
    extras_require={
        "server": ["uvicorn>=0.22.0",
                   "fastapi>=0.100.0",
                   "pydantic-settings>=2.0.1",
                   "sentence_transformers>=2.2.2",
                   ],
    },
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
