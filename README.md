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

3. Launch the service.

```
docker-compose up
```

## Training

When training the transformer model with the Shrunk database, each iteration took a significant amount of time (approximately 60 seconds per iteration on an Apple M2 Max with 32GB of RAM). Consequently, it is advisable to train the model in the cloud rather than on-device.

Instructions for training the model on [Amazon Web Services](https://aws.amazon.com/) coming soon.

## Citations

- Hugging Face Inc, [Transformers: State-of-the-Art Natural Language Processing](https://aclanthology.org/2020.emnlp-demos.6/)
- Google Research, [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](http://jmlr.org/papers/v21/20-074.html)
- Google Research, [LongT5: Efficient Text-To-Text Transformer for Long Sequences](https://aclanthology.org/2022.findings-naacl.55)
