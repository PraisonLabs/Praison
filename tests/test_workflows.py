import pytest
from praison.workflows import parse_workflow

def test_parse_simple_workflow(tmp_path):
    wf = tmp_path / 'test.yaml'
    wf.write_text('agents:\n  - name: test\ntasks:\n  - do: something')
    result = parse_workflow(str(wf))
    assert 'agents' in result
    assert result['flow'] == 'sequential'
