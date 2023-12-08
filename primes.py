"""List of prime numbers generator."""
def is_prime(val):
    if val < 2:
        return False
    for i in range(2, int(val ** 0.5) + 1):
        if val % i == 0:
            return False
    return True

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("number_of_primes should be a positive integer")
    list = []
    num = 2
    while len(list) < number_of_primes:
        if is_prime(num):
            list.append(num)
        num += 1
    return list
