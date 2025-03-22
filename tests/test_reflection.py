import pytest
from praison.reflection import ReflectionEngine

def test_reflection_engine_init():
    engine = ReflectionEngine()
    assert engine.max_iterations == 3
    assert engine.threshold == 0.8

def test_custom_threshold():
    engine = ReflectionEngine(max_iterations=5, threshold=0.9)
    assert engine.max_iterations == 5
