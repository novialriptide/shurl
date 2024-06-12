# Shurl [![license: Apache-2.0](https://img.shields.io/github/license/novialriptide/shurl)](./LICENSE)

Shurl is Shrunk's artificial intelligence platform. This is not meant to be a standalone project and is supposed to be a submodule for [Shrunk](https://github.com/oss/shrunk), an open-source URL shortener for Rutgers University.

> [!NOTE]
> This research project is not officially endorsed by Rutgers University.

## Features

- [ ] Produces title suggestions for the shortened URL
- [ ] Interactive web app for demonstration purposes

## Get Started

We use [pre-commit](https://pre-commit.com/) to ensure that all committed code does not violate the [Ruff](https://docs.astral.sh/ruff/) linter.

1. Fork, then clone the repository
2. Install [pre-commit](https://pre-commit.com/)

```
pip install pre-commit --break-system-packages && pre-commit install
```

### Build

Launch the service.

```
docker-compose up app
```

### Test

Check if your changes aren't regressive.

```
docker-compose up test
```

## Citations

- Hugging Face Inc, [Transformers: State-of-the-Art Natural Language Processing](https://aclanthology.org/2020.emnlp-demos.6/)
- Google Research, [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](http://jmlr.org/papers/v21/20-074.html)
- Google Research, [LongT5: Efficient Text-To-Text Transformer for Long Sequences](https://aclanthology.org/2022.findings-naacl.55)
