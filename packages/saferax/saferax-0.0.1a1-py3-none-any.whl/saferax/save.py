import os
import math
import json
import jax.numpy as jnp

from huggingface_hub import HfApi
from safetensors.numpy import save_file

from saferax.utils import get_state_dict


def save_as_shards(
    state_dict: dict,
    path: str,
    max_shard_size: int = 2 * 1024**3
):
    total_size = sum(tensor.nbytes for tensor in state_dict.values())
    num_shards = math.ceil(total_size / max_shard_size)
    
    # Calculate tensors per shard
    tensors_per_shard = math.ceil(len(state_dict) / num_shards)
    
    # Save shards
    for shard_idx in range(num_shards):
        shard_dict = {}
        start_idx = shard_idx * tensors_per_shard
        end_idx = min((shard_idx + 1) * tensors_per_shard, len(state_dict))
        
        # Get subset of tensors for this shard
        keys = list(state_dict.keys())[start_idx:end_idx]
        for key in keys:
            shard_dict[key] = state_dict[key]
            
        # Save shard with format model-00001-of-00005.safetensors
        shard_name = f"model-{str(shard_idx+1).zfill(5)}-of-{str(num_shards).zfill(5)}.safetensors"
        save_file(shard_dict, os.path.join(path, shard_name))
        
    # Save index file with metadata
    if num_shards > 1:
        index = {
            "metadata": {
                "total_size": total_size,
                "num_shards": num_shards
            },
            "weight_map": {name: f"model-{i//tensors_per_shard + 1:05d}-of-{num_shards:05d}.safetensors"
                          for i, name in enumerate(state_dict.keys())}
        }
        
        with open(os.path.join(path, "model.safetensors.index.json"), "w") as f:
            json.dump(index, f, indent=2)


def save_model(
    model,
    path: str,
    shard: bool = False,
    max_shard_size: int = 2 * 1024**3,
    push_to_hub: bool = False,
    repo_id: str = None,
    commit_message: str = None
):
    assert not push_to_hub or repo_id, "repo_id must be provided if push_to_hub is True"
    
    state_dict = get_state_dict(model)
    os.makedirs(path, exist_ok=True)
    
    if not shard:
        save_file(state_dict, os.path.join(path, "model.safetensors"))
    else:
        save_as_shards(state_dict, path, max_shard_size)

    if push_to_hub:
        api = HfApi()
        
        # Create repo if it doesn't exist
        api.create_repo(repo_id, exist_ok=True)
        
        # Upload all files in the directory
        files = [f for f in os.listdir(path)]
        
        for file in files:
            api.upload_file(
                path_or_fileobj=os.path.join(path, file),
                path_in_repo=file,
                repo_id=repo_id,
                commit_message=commit_message or f"Upload {file}"
            )
