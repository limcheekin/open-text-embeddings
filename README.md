# Open Source Text Embedding Models with OpenAI API-Compatible Endpoint

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

Many open source projects support the compatibility of the `completions` and the `chat/completions` endpoints of the OpenAI API, but do not support the `embeddings` endpoint.

The goal of this project is to create an OpenAI API-compatible version of the `embeddings` endpoint, which serves open source sentence-transformers models and other models supported by the LangChain's [HuggingFaceEmbeddings](https://api.python.langchain.com/en/latest/embeddings/langchain.embeddings.huggingface.HuggingFaceEmbeddings.html), HuggingFaceInstructEmbeddings and HuggingFaceBgeEmbeddings class.

## Supported Text Embeddings Models

Below is a compilation of open-source models that are tested via the `embeddings` endpoint:

- [BAAI/bge-large-en](https://huggingface.co/BAAI/bge-large-en)
- [intfloat/e5-large-v2](https://huggingface.co/intfloat/e5-large-v2)
- [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- [sentence-transformers/all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2)
- [universal-sentence-encoder-large/5](https://tfhub.dev/google/universal-sentence-encoder-large/5) (Please refer to the `universal_sentence_encoder` branch for more details)

The models mentioned above have undergone personal testing and verification. It is worth noting that all sentence-transformers models are expected to perform seamlessly with the endpoint.

## Standalone FastAPI Server

To run the embeddings endpoint locally as a standalone FastAPI server, follow these steps:

1. Install the dependencies by executing the following commands:

   ```bash
   pip install --no-cache-dir -r server-requirements.txt
   pip install --no-cache-dir uvicorn
   ```

2. Run the server with the desired model using the following command which enabled normalize embeddings (Omit the `NORMALIZE_EMBEDDINGS` if the model don't support normalize embeddings):

   ```bash
   MODEL=intfloat/e5-large-v2 NORMALIZE_EMBEDDINGS=1 python -m open.text.embeddings.server
   ```

   If a GPU is detected in the runtime environment, the server will automatically execute using the `cuba` mode. However, you have the flexibility to specify the `DEVICE` environment variable to choose between `cpu` and `cuba`. Here's an example of how to run the server with your desired configuration:

   ```bash
   MODEL=intfloat/e5-large-v2 NORMALIZE_EMBEDDINGS=1 DEVICE=cpu python -m open.text.embeddings.server
   ```

   This setup allows you to seamlessly switch between CPU and GPU modes, giving you control over the server's performance based on your specific requirements.

3. You will see the following text from your console once the server has started:

   ```bash
   INFO:     Started server process [19705]
   INFO:     Waiting for application startup.
   INFO:     Application startup complete.
   INFO:     Uvicorn running on http://localhost:8000 (Press CTRL+C to quit)
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
   pip install --no-cache-dir -r test-requirements.txt
   ```

2. Execute the cells in the notebook to test the embeddings endpoint.

## Contributions

[Vokturz](https://github.com/Vokturz) contributed [#2](https://github.com/limcheekin/open-text-embeddings/pull/2): support for CPU/GPU choice and initialization before starting the app.
