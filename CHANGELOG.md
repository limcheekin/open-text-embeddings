# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.4] - 2024-02-09

- feat: Added dimensions to request parameter of the embeddings endpoint.
- fix: Changed langchain imports to langchain_community.
- fix: GZipRequestMiddleware caused request error in fastapi 0.109.2.
- doc: Updated readme for download model step and fix open-in-colab badge.

## [1.0.3] - 2023-11-13

- [jayxuz](https://github.com/jayxuz) contributed [#5](https://github.com/limcheekin/open-text-embeddings/pull/5): improved OpenAI API compatibility, better support for previous versions of Python (start from v3.7), better defaults and bug fixes.
- Normalize embeddings enabled by default.
- Added `VERBOSE` environment variable to support verbose logging, disabled by default.
- Support `openai` package version >= 1.0.0.

## [1.0.2] - 2023-10-11

- [#3](https://github.com/limcheekin/open-text-embeddings/issues/3) Added gzip compression to web request and response.

## [1.0.1] - 2023-09-27

- Fixed readme and package publishing workflow, no changes to code.

## [1.0.0] - 2023-09-27

- Initial release 🎉
- [Vokturz](https://github.com/Vokturz) contributed [#2](https://github.com/limcheekin/open-text-embeddings/pull/2): support for CPU/GPU choice and initialization before starting the app.
