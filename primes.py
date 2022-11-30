"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if number_of_primes <= 0:
        raise ValueError

    b = 2
    prime = True
    while len(list) < number_of_primes:
            for a in range(2,b):
                if b % a == 0:
                    b = False

    if b is prime:
        list.append(b)
        b += 1

    return list
