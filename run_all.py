import os
import subprocess
import sys
from time import sleep

import requests

SAMPLES = ['callbacks_sample', 'opbank']


def wait_mock_server():
    for i in range(5):
        sleep(0.5)
        try:
            requests.delete("http://localhost:8888/admin/storage")
            return
        except:
            pass


def main():
    for sample in SAMPLES:
        samples_path = os.path.join('.', sample)
        process_args = ['meeshkan', 'mock', '--callback-dir', 'callbacks']
        if 'opbank' == sample:
            process_args.append('specs')
        with subprocess.Popen(process_args, cwd=samples_path) as mock_process:
            try:
                if os.path.isdir(samples_path):
                    wait_mock_server()
                    my_env = os.environ.copy()
                    my_env["PYTHONPATH"] = '../'
                    ret = subprocess.call(["pytest"], cwd=samples_path, env=my_env)
                    if ret != 0:
                        return ret
            finally:
                mock_process.kill()

    return 0


if __name__ == "__main__":
    sys.exit(main())
