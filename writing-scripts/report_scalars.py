"""Simple example to check integrations are correctly setup."""
import math
import time

import meeshkan


SLEEP_INTERVAL_SECS = 1  # Sleep this many seconds
ITERATIONS = 25


def main():
    for i in range(ITERATIONS):
        meeshkan.report_scalar("y", math.sin(i * 2 * math.pi / ITERATIONS))
        time.sleep(SLEEP_INTERVAL_SECS)


if __name__ == '__main__':
    main()
