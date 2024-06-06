# Shurl ![license: Apache-2.0](https://img.shields.io/github/license/novialriptide/shurl) ![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)

Shurl is Shrunk's artificial intelligence platform. This is not meant to be a standalone project and is supposed to be a submodule for [Shrunk](https://github.com/oss/shrunk), an open-source URL shortener for Rutgers University.

> [!NOTE]
> This research project is not officially endorsed by Rutgers University.

## Features

- [ ] Produces suggestions for a shortened URL given a valid URL
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

- Google Brain, [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.3215)
- Christopher Olah, [Understanding LSTMs](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- Apple Machine Learning Research, [Compressing LLMs: The Truth is Rarely Pure and Never Simple](https://arxiv.org/abs/2310.01382)
