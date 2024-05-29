# Shurl

Shurl is Shrunk's artificial intelligence platform. [Shrunk](https://github.com/oss/shrunk) is Rutgers University's official open-source URL shortener. This is not meant to be a standalone project and is supposed to be a submodule for [Shrunk](https://github.com/oss/shrunk).

## Get Started

We use [Poetry](https://python-poetry.org/) to manage our Python dependencies, you can learn more about it [here](https://python-poetry.org/docs/). We also use [Docker](https://docker.io/) to create consistent development and production environments by containerizing our applications.

1. Clone this respository
2. Install [pre-commit](https://pre-commit.com/)
3. Install the git hook scripts

```bash
pre-commit install
```

4. Use Docker Compose to launch the service with the following command:

```bash
docker-compose up
```
