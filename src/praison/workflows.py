"""No-code workflow definitions via YAML."""

import yaml
from typing import Dict, List

def parse_workflow(yaml_path: str) -> Dict:
    with open(yaml_path) as f:
        config = yaml.safe_load(f)
    return {
        'agents': config.get('agents', []),
        'tasks': config.get('tasks', []),
        'flow': config.get('flow', 'sequential')
    }
