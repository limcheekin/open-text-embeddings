# Open Source Text Embedding Models with OpenAI API Compatible Endpoint

Many open source projects support the compatibility of the `completion` and the `chat_completion` endpoint of the OpenAI API, but not support the `embeddings` endpoint.

The project goal is to create OpenAI API compatible version of the `embeddings` endpoint serving open source models such as `intfloat/e5-large-v2`, `sentence-transformers/all-MiniLM-L6-v2`, `sentence-transformers/all-mpnet-base-v2` and other sentence-transformers models supported by the LangChain's [HuggingFaceEmbedding](https://api.python.langchain.com/en/latest/embeddings/langchain.embeddings.huggingface.HuggingFaceEmbeddings.html) class.

The codes of the repo are quick hack over the weekend, it is working functionally but far from optimal. Appreciate your contributions to improve the code quality.

## Standalone FastAPI Server

To run the embeddings endpoint locally as a standalone FastAPI server, you need to install the dependencies with the following commands:

```bash
pip install -r --no-cache-dir server-requirements.txt
pip install --no-cache-dir uvicorn
```

Then run:

```bash
MODEL=intfloat/e5-large-v2 python -m open.text.embeddings.server
```

## AWS Lambda Function

To deploy the embeddings endpoint as a AWS Lambda Function using GitHub Actions, you need to add the `AWS_KEY` and `AWS_SECRET` to repository secrets, for example at https://github.com/limcheekin/open-text-embeddings/settings/secrets/actions.

Then, you can trigger the `Deploy Dev` and `Remove Dev` GitHub Action manually to deploy or remove the AWS Lambda Function.

## Testing the Embeddings Endpoint

To test the embeddings endpoint, the repo included a `embeddings.ipynb` notebook with a LangChain-compatible `OpenAIEmbedding` class.

First, you need to install the dependencies with the following commands:

```bash
pip install -r --no-cache-dir test-requirements.txt
```

Then, you can start executing the cells of the notebook.
