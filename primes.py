"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if number_of_primes <= 0:
        raise ValueError

    a = 0
    b = 2
    prime = True
    while len(list) < number_of_primes:
            for c in range(2,b):
                if b % c == 0:
                    prime = False

    if prime:
        list.append(b)
        a += 1
    b += 1
    prime = True

    return list
