import subprocess
import os
import sys
from time import sleep

SAMPLES = ['callback_sample', 'opbank']
def main():
    mock_process = None
    for sample in SAMPLES:
        try:
            samples_path = os.path.join('.', sample)
            if os.path.isdir(samples_path):
                mock_process = subprocess.Popen(["meeshkan", "mock"], cwd=samples_path)
                sleep(5)
                my_env = os.environ.copy()
                my_env["PYTHONPATH"] = '../'
                ret = subprocess.call(["pytest"], cwd=samples_path, env=my_env)
                if ret != 0:
                    return ret
        finally:
            if mock_process is not None:
                #mock_process.kill()
                sleep(5)


    return 0


if __name__ == "__main__":
    sys.exit(main())
