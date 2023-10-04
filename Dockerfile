# REF: https://aws.amazon.com/blogs/aws/new-for-aws-lambda-container-image-support/
# The download size of `python:3.10-slim-bullseye` is **45MB**¹. Its uncompressed on-disk size is **125MB**¹.
# (1) The best Docker base image for your Python application (March 2023). https://pythonspeed.com/articles/base-image-python-docker-images/.
# (2) Reduce the size of container images with DockerSlim. https://developers.redhat.com/articles/2022/01/17/reduce-size-container-images-dockerslim.
FROM debian:bullseye-slim AS build-image

ARG MODEL
ENV MODEL=${MODEL}

COPY ./download.sh ./

# Install build dependencies
RUN apt-get update && \
    apt-get install -y git-lfs

RUN chmod +x *.sh && \
    ./download.sh && \
    rm *.sh

# Stage 3 - final runtime image
# Grab a fresh copy of the Python image
FROM public.ecr.aws/lambda/python:3.11

ARG MODEL

RUN mkdir -p ${MODEL}
COPY --from=build-image ${MODEL} ${MODEL}
RUN pip install --upgrade pip setuptools && \
    pip install --no-cache-dir open-text-embeddings[server] mangum

CMD [ "open.text.embeddings.server.aws.handler" ]
