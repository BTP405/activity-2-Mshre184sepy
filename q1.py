# Question1
# Write a Python function getPrimeNumbers(n) which returns a list containing all prime numbers between 2 and n.
# Create a helper function to determine if a particular number is prime and then use a comprehension to generate your list.

def is_prime(number):
    """Checking if a number is prime or not."""
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def getPrimeNumbers(n):
    """Returns a list of prime numbers between the range 2,n"""
    return [Num for Num in range(2, n + 1) if is_prime(Num)]

# testing
n = 44
prime_numbers = getPrimeNumbers(n)
print(f"Prime numbers between 2 and {n}: {prime_numbers}")

