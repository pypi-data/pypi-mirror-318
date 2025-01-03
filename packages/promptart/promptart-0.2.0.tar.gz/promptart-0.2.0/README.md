# promptart

[![CI - Tests](https://github.com/manuelkonrad/promptart/actions/workflows/tests.yml/badge.svg)](https://github.com/manuelkonrad/promptart/actions/workflows/tests.yml)
[![CI - Bandit](https://github.com/manuelkonrad/promptart/actions/workflows/bandit.yml/badge.svg)](https://github.com/manuelkonrad/promptart/actions/workflows/bandit.yml)
[![CI - Build](https://github.com/manuelkonrad/promptart/actions/workflows/build.yml/badge.svg)](https://github.com/manuelkonrad/promptart/actions/workflows/build.yml)

[![License - MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://spdx.org/licenses/MIT.html)
[![PyPI - Version](https://img.shields.io/pypi/v/promptart.svg)](https://pypi.org/project/promptart)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/promptart.svg)](https://pypi.org/project/promptart)
[![Python Project Management - Hatch](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![Linting - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Types - Mypy](https://img.shields.io/badge/types-Mypy-blue.svg)](https://github.com/python/mypy)
[![Security - Bandit](https://img.shields.io/badge/security-Bandit-yellow.svg)](https://github.com/PyCQA/bandit)

Simple frontend for accessing image and speech generation APIs. Made with Streamlit.

Currently supported:

- Black Forest Labs Flux (Text-to-Image, In/Out-Painting, Image Variation, Structural Conditioning)
- OpenAI Dall-E (Text-to-Image)
- OpenAI TTS (Text-to-Speech)

## Table of Contents

- [Getting Started](#getting_started)
- [License](#license)

## Getting Started

Install `promptart` using `pipx`:

```console
pipx install promptart
```

Alternatively, install `promptart` using `pip`:

```console
pip install --user promptart
```

Start the application:

```console
promptart
```

Additional `streamlit` arguments can be appended. For example, to change the server port:

```console
promptart --server.port 5000
```

The API keys for authentication can be provided in the following ways:

1. Setting environment variables `BFL_API_KEY` / `OPENAI_API_KEY`.
2. Creating `~/promptart/config.json` populated with parameters `bfl_api_key` / `openai_api_key`.
3. If 1. and 2. are not set, the API keys can also be provided in the frontend.

Further information about creating API keys:

- [Black Forest Labs Documentation](https://docs.bfl.ml/quick_start/create_account)
- [OpenAI Documentation](https://platform.openai.com/docs/quickstart)

To limit access to the frontend, a simple password check can be enabled by
setting the environment variable `PROMPTART_PASSWORD`.

## License

`promptart` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
