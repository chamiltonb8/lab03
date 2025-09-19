#Include any necessary imports here:
from math import sqrt


# Problem 1: Euclidean Distance
def euclidean_distance(a, b):
    (x1, y1), (x2, y2) = a, b
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(euclidean_distance((1, 3), (7, 11)))

# Problem 2: n + nn + nnn
def sum_ns(n):
    if n < 0 or n > 9:
        return "Input must be a single digit (0-9)"
    nn = int(f"{n}{n}")
    nnn = int(f"{n}{n}{n}")
    total = n + nn + nnn
    return total
print (sum_ns(2))

# Problem 3: Perfect Square
def perfect_square(n):
    root = sqrt(n)
    if root * root == n:
        return f"{n} is a perfect square of {root}"
    else:
        return False
print(perfect_square(24))
print(perfect_square(25))

# Problem 4: Palindrome
def is_palindrome():
    s = input("Enter a string: ")
    if s == s[::-1]:
        return True
    else:
        return False
print(is_palindrome())

# Problem 5: Letter Types
def count_letter_types():
    s = input("Enter a string: ")
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    space = sum(1 for c in s if c.isspace())
    return f"{{'upper': {upper}, 'lower': {lower}, 'space': {space}}}"
print(count_letter_types())

# Problem 6: Word Lengths
def word_lengths():
    s = input("s = ")
    words = s.split()
    lengths_dict = {}
    for word in words:
        l = len(word)
        lengths_dict.setdefault(l, []).append(word)
    return lengths_dict
print(word_lengths())

# Problem 7: N List
def n_list(n):
    if not isinstance(n, int) or n < 1 or n>9:
        return None
    
    result = []
    for i in range (0, n*100 + 1):
        if str(n) in str(i) and i % n ==0:
            result.append(i)
    return result
print(n_list(3))

# Problem 8: Tens Dictionary
def tens_dict():
    return {i: i/100 for i in range(0, 201, 10)}
print(tens_dict())
