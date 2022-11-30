"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if number_of_primes < 1:
        raise ValueError
    a = 2
    while number_of_primes != 0:
        prime = True
        for i in range(2, a):
            if a % i == 0:
                prime = False
        if prime:
            list.append(a)
            number_of_primes -= 1
        a += 1

    return list
