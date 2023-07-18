# REF: https://aws.amazon.com/blogs/aws/new-for-aws-lambda-container-image-support/
# The download size of `python:3.10-slim-bullseye` is **45MB**¹. Its uncompressed on-disk size is **125MB**¹.
# (1) The best Docker base image for your Python application (March 2023). https://pythonspeed.com/articles/base-image-python-docker-images/.
# (2) Reduce the size of container images with DockerSlim. https://developers.redhat.com/articles/2022/01/17/reduce-size-container-images-dockerslim.
FROM debian:bullseye-slim AS build-image

COPY ./download_universal-sentence-encoder-large-v5.sh ./

# Install build dependencies
RUN apt-get update && \
    apt-get install -y curl

RUN chmod +x *.sh && \
    ./download_universal-sentence-encoder-large-v5.sh && \
    rm *.sh

# Stage 3 - final runtime image
# Grab a fresh copy of the Python image
FROM public.ecr.aws/lambda/python:3.10

RUN mkdir universal-sentence-encoder-large && mkdir -p open/text/embeddings/server 
COPY --from=build-image universal-sentence-encoder-large universal-sentence-encoder-large
COPY open/text/embeddings/server ./open/text/embeddings/server
COPY server-requirements.txt ./
RUN pip install --no-cache-dir -r server-requirements.txt

CMD [ "open.text.embeddings.server.aws.handler" ]
