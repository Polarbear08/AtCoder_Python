"""
Hash function SHA-256
author: polarbear08

"""

from math import sqrt

def calculate_initial_hash():
    """Calculate initial 32byte hash."""
    first_eight_primes = []
    initial_hash = []

    prime_generator = 1
    block_num = 8
    for _ in range(block_num):
        first_eight_primes.append(next(prime_generator))







# calculate round constants



#