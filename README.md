# Shurl [![build system: Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/) [![code style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) [![license: Apache-2.0](https://img.shields.io/github/license/novialriptide/shurl)](./LICENSE)

Shurl is Shrunk's artificial intelligence platform. This is not meant to be a standalone project and is supposed to be a submodule for [Shrunk](https://github.com/oss/shrunk), an open-source URL shortener for Rutgers University.

> [!NOTE]
> This research project is not officially endorsed by Rutgers University.

## Features

- [ ] Produces title suggestions for the shortened URL
- [ ] Interactive web app for demonstration purposes

## Get Started

We use [Poetry](https://python-poetry.org/) to manage our Python dependencies, you can learn more about it [here](https://python-poetry.org/docs/). We also use [Docker](https://docker.io/) to create consistent development and production environments by containerizing our applications. We also use [pre-commit](https://pre-commit.com/) to ensure the project stays clean and maintainable during its lifespan as deep-learning is a complex topic.

1. Clone this respository
2. Install [pre-commit](https://pre-commit.com/)
3. Install the git hook scripts

```bash
pre-commit install
```

4. You're ready to contribute

### Build

Launch the service.

```bash
docker-compose up app
```

### Test

Check if your changes aren't regressive.

```bash
docker-compose up test
```

## Citations

- Hugging Face Inc, [Transformers: State-of-the-Art Natural Language Processing](https://aclanthology.org/2020.emnlp-demos.6/)
- Google Research, [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://huggingface.co/google-t5/t5-small)
