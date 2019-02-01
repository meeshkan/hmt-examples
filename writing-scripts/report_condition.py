"""Simple example to check integrations are correctly setup."""
import random
import time

import meeshkan

SLEEP_INTERVAL_SECS = 1
RANDOM_NUMBER_THRESHOLD = 0.8
ITERATIONS = 30


def main():
    meeshkan.add_condition("random number", condition=lambda number: number > RANDOM_NUMBER_THRESHOLD)
    for i in range(ITERATIONS):
        new_random_number = random.uniform(0, 1)
        meeshkan.report_scalar("random number", new_random_number)
        time.sleep(SLEEP_INTERVAL_SECS)


if __name__ == '__main__':
    main()
