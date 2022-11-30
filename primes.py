"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if number_of_primes <= 0:
        raise ValueError

    b = 2
    while len(list) < number_of_primes:
        prime = True

        for a in range(2,b):
            if b % a == 0:
                prime = False

    if b is prime:
        list.append(b)
        number_of_primes -= 1
    b += 1

    return list
