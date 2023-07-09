# Open Source Text Embedding Models with OpenAI API-Compatible Endpoint

Many open source projects support the compatibility of the `completions` and the `chat/completions` endpoints of the OpenAI API, but do not support the `embeddings` endpoint.

The goal of this project is to create an OpenAI API-compatible version of the `embeddings` endpoint, which serves open source models such as `intfloat/e5-large-v2`, `sentence-transformers/all-MiniLM-L6-v2`, `sentence-transformers/all-mpnet-base-v2`, and other sentence-transformers models supported by the LangChain's [HuggingFaceEmbeddings](https://api.python.langchain.com/en/latest/embeddings/langchain.embeddings.huggingface.HuggingFaceEmbeddings.html) class.

The code in this repository is a quick hack developed over the weekend. While it functions correctly, it is far from optimal. We appreciate your contributions to improve the code quality.

## Standalone FastAPI Server

To run the embeddings endpoint locally as a standalone FastAPI server, follow these steps:

1. Install the dependencies by executing the following commands:

```bash
pip install -r --no-cache-dir server-requirements.txt
pip install --no-cache-dir uvicorn
```

2. Run the server with the desired model using the following command:

```bash
MODEL=intfloat/e5-large-v2 python -m open.text.embeddings.server
```

## AWS Lambda Function

To deploy the embeddings endpoint as an AWS Lambda Function using GitHub Actions, follow these steps:

1. Add your AWS credentials (`AWS_KEY` and `AWS_SECRET`) to the repository secrets. You can do this by navigating to https://github.com/username/open-text-embeddings/settings/secrets/actions.

2. Manually trigger the `Deploy Dev` or `Remove Dev` GitHub Actions to deploy or remove the AWS Lambda Function.

## Testing the Embeddings Endpoint

To test the embeddings endpoint, this repository includes an `embeddings.ipynb` notebook with a LangChain-compatible `OpenAIEmbeddings` class.

To get started:

1. Install the dependencies by executing the following command:

```bash
pip install -r --no-cache-dir test-requirements.txt
```

2. Execute the cells in the notebook to test the embeddings endpoint.
