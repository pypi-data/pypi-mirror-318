# Saferax: Loading Safetensor from HF to Equinox

![Saferax Logo](imgs/logo.jpg)

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![PyPI version](https://badge.fury.io/py/saferax.svg)](https://badge.fury.io/py/saferax)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

Saferax is a lightweight utility library that enables seamless loading of SafeTensor files from Hugging Face Hub into Equinox models. It provides efficient handling of model weights with support for sharded loading and direct Hugging Face Hub integration.

## Features

- 🔄 Load SafeTensor files directly into Equinox models
- 💾 Support for sharded model weights
- 🤗 Direct integration with Hugging Face Hub
- 📦 Simple to use API

## Installation

Saferax can be installed using pip like every python library and requires Python 3.11 or later.

```text
pip install saferax
```

## Saving Models

You can save your models in two ways with Saferax:
1. Save to your computer: Consolidated or Sharded.
2. Save directly to Hugging Face Hub

To save locally you just pass the equinox model and path to save it locally:

```python
sx.save_model(model, "path/to/save")
```

To save model over shards of safetensor file you can pass `shard=True` and `max_shard_size`, the name scheme is same as what hugging face uses so you need not worry about that.

```python
sx.save_model(
    model,
    "path/to/save",
    shard=True,
    max_shard_size=2 * 1024 * 1024
)
```

## Push to Hugging Face Hub

With Saferax you can push your model directly to HF hub, just add the `repo_id` & `commit_message` and saferax will take care of the rest.

```python
sx.save_model(
    model,
    "path/to/save",
    push_to_hub=True,
    repo_id="your-username/your-model",
    commit_message="Update model weights"
)
```

## Loading Models

You can easily use Saferax to load models from Hugging Face Hub into Equinox. It takes care of downloading, saving, and converting the model files for you.

```
loaded_model = sx.load_model(
    model,
    "your-username/your-model",
)
```

