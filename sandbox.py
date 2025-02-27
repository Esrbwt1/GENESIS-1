# sandbox.py
import subprocess

def run_in_sandbox(script):
    """
    Executes a Python script in a subprocess to simulate sandboxing.
    
    Args:
        script (str): Path to the Python script.
    
    Returns:
        tuple: (stdout, stderr) from the subprocess execution.
    """
    result = subprocess.run(["python", script], capture_output=True, text=True)
    return result.stdout, result.stderr

if __name__ == "__main__":
    # Test by running a simple script (create a test_script.py if needed)
    out, err = run_in_sandbox("test_script.py")
    print("Sandbox Output:", out)
    print("Sandbox Errors:", err)