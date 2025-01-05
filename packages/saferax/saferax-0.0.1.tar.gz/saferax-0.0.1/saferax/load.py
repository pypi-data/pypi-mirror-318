import os
import json
import numpy as np
import equinox as eqx
import jax.numpy as jnp
import jax.tree_util as jtu

from typing import Mapping
from safetensors import safe_open

from saferax.utils import (
    fs,
    download_model,
    get_device_array,
)


def _load_sharded_model(file_paths: Mapping[str, str], device: str = "cpu") -> Mapping[str, jnp.ndarray]:
    weights = {}
    shard_to_tensors = {}

    with open(file_paths["model.safetensors.index.json"]) as f:
        index = json.load(f)

    # Build mapping of shard file to tensor names
    for tensor_name, shard_file in index['weight_map'].items():
        if shard_file not in shard_to_tensors:
            shard_to_tensors[shard_file] = []
        shard_to_tensors[shard_file].append(tensor_name)

    # Load each shard file once and get all its tensors
    for shard_file, tensor_names in shard_to_tensors.items():
        shard_path = file_paths[shard_file]
        with safe_open(shard_path, framework="numpy") as f:                                 # type: ignore
            for tensor_name in tensor_names:
                weights[tensor_name] = get_device_array(f.get_tensor(tensor_name), device)

    return weights


def load_model(model, path: str, device: str = "cpu", num_threads = 10) -> eqx.Module:
    """Load weights from safetensors file(s) into an Equinox model.

    Args:
        model: The Equinox model to load weights into
        path: Hugging Face model path (e.g. "gpt2")
        device: Device to load tensors to ("cpu" or "gpu")

    Returns:
        Updated Equinox model with loaded weights
    """

    model_clone = jtu.tree_map(lambda x: x, model)

    files = None
    if os.path.isdir(path):
        files = {f: os.path.join(path, f) for f in os.listdir(path)}
    else:
        files = download_model(path, num_threads=num_threads)

    weights = None
    if "model.safetensors.index.json" in files:
        weights = _load_sharded_model(files, device)
    else:
        with safe_open(files["model.safetensors"], framework="numpy") as f:                # type: ignore
            weights = {k: get_device_array(f.get_tensor(k), device) for k in f.keys()}
    
    # Get the structure of the model
    leaves, treedef = jtu.tree_flatten(model_clone)
    
    # Convert weights dict to list matching the model's leaf order
    new_leaves = []
    for leaf in leaves:
        if isinstance(leaf, (jnp.ndarray, np.ndarray)):  # only replace arrays
            # Find matching weight from state dict
            key = next(k for k, v in weights.items() if v.shape == leaf.shape)
            new_leaves.append(weights[key])
        else:
            new_leaves.append(leaf)  # keep non-array leaves as is
            
    # Reconstruct the model with new weights
    return jtu.tree_unflatten(treedef, new_leaves)