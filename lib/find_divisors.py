# -*- coding: utf8 -*-

__author__ = "polarbear08"
__date__ = "16 May 2019"


def find_divisors(n: int) -> list:
    """Return divisors of positive integer n

    Args:
        n: Positive integer

    Returns:
        divisors: Divisors of n

    """

    divisors = []
    for i in range(1, n):
        if i*i > n:
            break

        elif i*i == n:
            divisors.append(i)
            break

        elif n % i == 0:
            divisors.append(i)
            divisors.append(n//i)

    return divisors

