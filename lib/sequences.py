#!/usr/bin/env python3

def print_fibonacci(n):
    # If n is 0, print an empty list
    if n == 0:
        print([])
        return

    # Start the sequence with first two numbers
    fib = [0, 1]

    # If n is 1, return only [0]
    if n == 1:
        print([0])
        return

    # Generate the rest of the sequence up to n elements
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])

    print(fib)

