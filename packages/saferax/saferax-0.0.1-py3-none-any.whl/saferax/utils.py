import os
import jax
import equinox as eqx
import jax.tree_util as jtu

from typing import Mapping
from jax import numpy as jnp
from concurrent.futures import ThreadPoolExecutor
from huggingface_hub import hf_hub_download, HfFileSystem


fs = HfFileSystem()


def download_model(model_id: str, num_threads: int = 10) -> Mapping[str, str]:
    downloaded_files = {}

    if not fs.exists(f"{model_id}/model.safetensors.index.json"):
        downloaded_files["model.safetensors"] = hf_hub_download(model_id, filename="model.safetensors")
    else:
        downloaded_files["model.safetensors.index.json"] = hf_hub_download(
            model_id,
            filename="model.safetensors.index.json"
        )

        st_files = fs.glob(f"{model_id}/model-*.safetensors")
        st_file_names = [os.path.basename(f) for f in st_files]

        if num_threads == 1:
            for st_file in st_file_names:
                downloaded_files[st_file] = hf_hub_download(model_id, filename=st_file)
        else:
            with ThreadPoolExecutor(num_threads) as pool:
                results = list(pool.map(hf_hub_download, [model_id]*len(st_file_names), st_file_names))

                for st_file, result in zip(st_file_names, results):
                    downloaded_files[st_file] = result


    return downloaded_files


def get_device_array(weight: jnp.ndarray, device: str) -> jnp.ndarray:
    weight = jnp.array(weight)

    if device == "cpu":
        return weight
    elif device == "gpu":
        return jax.device_put(weight, jax.devices("gpu")[0])
    elif device == "tpu":
        return jax.device_put(weight, jax.devices("tpu")[0])
    else:
        raise ValueError(f"Invalid device: {device}")


def get_state_dict(model):
    arrays, _ = eqx.partition(model, eqx.is_array)
    paths_and_values = jtu.tree_flatten_with_path(arrays)[0]
    
    state_dict = {}
    for (path, value) in paths_and_values:
        path_parts = []
        for p in path:
            if hasattr(p, 'name'):
                path_parts.append(p.name)
            elif hasattr(p, 'idx'):
                path_parts.append(str(p.idx))
        path_str = '.'.join(path_parts)
        state_dict[path_str] = value
        
    return state_dict
