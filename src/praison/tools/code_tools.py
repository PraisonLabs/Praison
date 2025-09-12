"""Code execution tools for agents."""

import subprocess
import tempfile

def run_python(code: str, timeout: int = 30) -> str:
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(code)
        f.flush()
        try:
            result = subprocess.run(
                ['python', f.name],
                capture_output=True, text=True, timeout=timeout
            )
            return result.stdout or result.stderr
        except subprocess.TimeoutExpired:
            return 'Execution timed out'
