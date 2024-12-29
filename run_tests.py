import subprocess
import os
import sys

def run_tests():
    base_dir = os.path.dirname(__file__)
    src_dir = os.path.join(base_dir, "src")
    if src_dir not in sys.path:
        sys.path.insert(0, src_dir)

    test_dir = os.path.join(base_dir, "tests")
    if not os.path.exists(test_dir):
        print(f"Error: Test directory not found at {test_dir}")
        return

    try:
        subprocess.check_call(["pytest", test_dir])
    except subprocess.CalledProcessError as e:
        print(f"Tests failed with error: {e}")
    else:
        print("All tests passed successfully!")

if __name__ == "__main__":
    run_tests()
