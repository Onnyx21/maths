from math import *


def is_prime(n):
        d = 2
        if n > 0:
            prime = True
            while d <= n/2:
                if n % d == 0:
                    prime = False
                    break
                else:
                    d += 1

            return prime

        else:
            return False


def calc_prime(n):
    primenumbers = []
    for i in range(1, n):
        if is_prime(i):
            primenumbers.append(i)

    return primenumbers


def dividers(n):
    div = []
    for i in range(1, n+1):
        if n % i == 0:
            div.append(i)
    return div


def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a
