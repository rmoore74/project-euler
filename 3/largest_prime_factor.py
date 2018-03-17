import math

def find_largest_prime(number):
    largest_prime = 0
    root = int(round(math.sqrt(number)))
    for i in range(2, root + 1):
        if number % i == 0 : 
            if is_prime_number(i) : 
                if i > largest_prime : 
                    largest_prime = i
    return largest_prime

def is_prime_number(number):
    for i in range(2, number/2):
        if number % i == 0 : return False
    return True

print find_largest_prime(600851475143)
