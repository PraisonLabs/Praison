"""Configuration management for Praison."""

import os
import yaml
from pathlib import Path

DEFAULT_CONFIG = {
    'default_llm': 'gpt-4',
    'max_agents': 10,
    'memory_backend': 'local',
    'reflection_enabled': True,
    'verbose': False,
}

def load_config(config_path: str = None) -> dict:
    if config_path and Path(config_path).exists():
        with open(config_path) as f:
            user_config = yaml.safe_load(f)
        return {**DEFAULT_CONFIG, **user_config}
    return DEFAULT_CONFIG.copy()
