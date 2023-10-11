# open-text-embeddings

[![PyPI](https://img.shields.io/pypi/v/open-text-embeddings)](https://pypi.org/project/open-text-embeddings/)
[![Open in Colab](https://camo.githubusercontent.com/84f0493939e0c4de4e6dbe113251b4bfb5353e57134ffd9fcab6b8714514d4d1/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/drive/1wfgfkt6xk3meSF5jWHDMqo6mL0ZvPw2f?usp=sharing)
[![Publish Python Package](https://github.com/limcheekin/open-text-embeddings/actions/workflows/publish.yml/badge.svg)](https://github.com/limcheekin/open-text-embeddings/actions/workflows/publish.yml)

Many open source projects support the compatibility of the `completions` and the `chat/completions` endpoints of the OpenAI API, but do not support the `embeddings` endpoint.

The goal of this project is to create an OpenAI API-compatible version of the `embeddings` endpoint, which serves open source sentence-transformers models and other models supported by the LangChain's [HuggingFaceEmbeddings](https://api.python.langchain.com/en/latest/embeddings/langchain.embeddings.huggingface.HuggingFaceEmbeddings.html), HuggingFaceInstructEmbeddings and HuggingFaceBgeEmbeddings class.

## ℹ️ Supported Text Embeddings Models

Below is a compilation of open-source models that are tested via the `embeddings` endpoint:

- [BAAI/bge-large-en](https://huggingface.co/BAAI/bge-large-en)
- [intfloat/e5-large-v2](https://huggingface.co/intfloat/e5-large-v2)
- [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- [sentence-transformers/all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2)
- [universal-sentence-encoder-large/5](https://tfhub.dev/google/universal-sentence-encoder-large/5) (Please refer to the `universal_sentence_encoder` branch for more details)

The models mentioned above have undergone testing and verification. It is worth noting that all sentence-transformers models are expected to perform seamlessly with the endpoint.

## 🔍 Demo

Try out open-text-embeddings in your browser:

[![Open in Colab](https://camo.githubusercontent.com/84f0493939e0c4de4e6dbe113251b4bfb5353e57134ffd9fcab6b8714514d4d1/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/drive/1wfgfkt6xk3meSF5jWHDMqo6mL0ZvPw2f?usp=sharing)

## 🖥️ Standalone FastAPI Server

To run the embeddings endpoint locally as a standalone FastAPI server, follow these steps:

1. Install the dependencies by executing the following commands:

   ```bash
   pip install --no-cache-dir open-text-embeddings[server]
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

## ☁️ AWS Lambda Function

To deploy the embeddings endpoint as an AWS Lambda Function using GitHub Actions, follow these steps:

1. [Fork](https://github.com/limcheekin/open-text-embeddings/fork) the repo.

2. Add your AWS credentials (`AWS_KEY` and `AWS_SECRET`) to the repository secrets. You can do this by navigating to https://github.com/username/open-text-embeddings/settings/secrets/actions.

3. Manually trigger the `Deploy Dev` or `Remove Dev` GitHub Actions to deploy or remove the AWS Lambda Function.

## 🧪 Testing the Embeddings Endpoint

To test the `embeddings` endpoint, the repository includes an [embeddings.ipynb](https://github.com/limcheekin/open-text-embeddings/blob/main/embeddings.ipynb) notebook with a LangChain-compatible `OpenAIEmbeddings` class.

To get started:

1. Install the dependencies by executing the following command:

   ```bash
   pip install --no-cache-dir open-text-embeddings openai
   ```

2. Execute the cells in the notebook to test the embeddings endpoint.

## ❓ Known Issues

1. Gzip compression for web request doesn't seems working in AWS Lambda Function.

## 🧑‍💼 Contributing

Contributions are welcome! Please check out the issues on the repository, and feel free to open a pull request.
For more information, please see the [contributing guidelines](CONTRIBUTING.md).

<a href="https://github.com/limcheekin/open-text-embeddings/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=limcheekin/open-text-embeddings" />
</a>

Thank you very much for the following contributions:

- [Vokturz](https://github.com/Vokturz) contributed [#2](https://github.com/limcheekin/open-text-embeddings/pull/2): support for CPU/GPU choice and initialization before starting the app.

## 📔 License

This project is licensed under the terms of the MIT license.

## 🗒️ Citation

If you utilize this repository, please consider citing it with:

```
@misc{open-text-embeddings,
  author = {Lim Chee Kin},
  title = {open-text-embeddings: Open Source Text Embedding Models with OpenAI API-Compatible Endpoint},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/limcheekin/open-text-embeddings}},
}
```
