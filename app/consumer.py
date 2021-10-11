#!/usr/bin/env python3

import math
import time

def pythagorean_theorem(a, b):
    # Sleep to emulate a longer-running task
    time.sleep(10)
    # Perform the task and return the result
    c = math.sqrt(a**2 + b**2)
    print(f'The length of the hypotenuse is {c}')
    return c
