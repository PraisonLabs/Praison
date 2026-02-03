"""Output guardrails for agent safety."""

from typing import Callable, List

class Guardrail:
    def __init__(self, check_fn: Callable, description: str = ''):
        self.check = check_fn
        self.description = description

class GuardrailManager:
    def __init__(self):
        self.guardrails: List[Guardrail] = []
    
    def add(self, guardrail: Guardrail):
        self.guardrails.append(guardrail)
    
    def validate(self, output: str) -> bool:
        return all(g.check(output) for g in self.guardrails)
