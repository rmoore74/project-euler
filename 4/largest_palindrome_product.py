def largest_palindrome_product():
    palindromes = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            palindrome = is_palindrome(product)
            if palindrome : palindromes.append(product)
    return max(palindromes)

def is_palindrome(number):
    num_str = str(number)
    reverse = num_str[::-1]
    if num_str == reverse:
        return True
    return False

print largest_palindrome_product()
