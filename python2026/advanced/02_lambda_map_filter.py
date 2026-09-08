# ─────────────────────────────────────────────
# ADV 02 — Lambda, map(), filter(), reduce()
# ─────────────────────────────────────────────
#
# WHAT IS A LAMBDA?
#   A lambda is a small, anonymous (nameless) function defined
#   in a single line. It can only contain one expression.
#   Use it when you need a short throwaway function — most
#   commonly as a key= argument when sorting.
#
# WHAT ARE map() AND filter()?
#   map()    — applies a function to every item in an iterable.
#   filter() — keeps only items where the function returns True.
#   Both return lazy iterators; wrap in list() to see the result.
# ─────────────────────────────────────────────

from functools import reduce

# --- Lambda (anonymous function) ---
# lambda parameters: expression
# Returns a function object — single expression only.

square = lambda x: x ** 2
print(square(5))           # 25

add = lambda a, b: a + b
print(add(3, 7))           # 10

# Ternary inside lambda
label = lambda n: "even" if n % 2 == 0 else "odd"
print(label(4))            # even

# --- Sorting with lambda (very common use-case) ---
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob",   "age": 25},
    {"name": "Carol", "age": 35},
]

sorted_by_age = sorted(people, key=lambda p: p["age"])
for p in sorted_by_age:
    print(p["name"], p["age"])
# Bob 25 / Alice 30 / Carol 35

words = ["banana", "apple", "cherry", "date"]
words.sort(key=lambda w: w[-1])   # sort by last character
print(words)

# --- map(func, iterable) ---
# Applies func to every item; returns a lazy iterator.
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)             # [2, 4, 6, 8, 10]

# map with a regular function
def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

temps_c = [0, 20, 37, 100]
temps_f = list(map(celsius_to_fahrenheit, temps_c))
print(temps_f)             # [32.0, 68.0, 98.6, 212.0]

# map over two iterables simultaneously
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(sums)                # [11, 22, 33]

# --- filter(func, iterable) ---
# Keeps items where func returns True; returns a lazy iterator.
numbers = range(-5, 6)
positives = list(filter(lambda x: x > 0, numbers))
print(positives)           # [1, 2, 3, 4, 5]

even_squares = list(filter(lambda x: x % 2 == 0,
                            map(lambda x: x**2, range(1, 11))))
print(even_squares)        # [4, 16, 36, 64, 100]

# --- reduce(func, iterable) ---
# Cumulatively applies func to reduce iterable to a single value.
nums = [1, 2, 3, 4, 5]

product = reduce(lambda acc, x: acc * x, nums)
print(product)             # 120  (1*2*3*4*5)

total = reduce(lambda acc, x: acc + x, nums, 0)  # 0 is initial value
print(total)               # 15

# Find maximum without max()
largest = reduce(lambda a, b: a if a > b else b, [3, 1, 9, 5])
print(largest)             # 9

# --- Composing map / filter / reduce ---
# Sum of squares of odd numbers from 1–10
result = reduce(
    lambda acc, x: acc + x,
    map(lambda x: x**2,
        filter(lambda x: x % 2 != 0, range(1, 11)))
)
print(result)              # 165  (1+9+25+49+81)

# Modern Pythonic equivalent (often preferred)
result2 = sum(x**2 for x in range(1, 11) if x % 2 != 0)
print(result2)             # 165

# --- operator module (faster alternative to lambdas) ---
import operator
nums = [3, 1, 4, 1, 5]
print(sorted(nums, key=operator.neg))   # [5, 4, 3, 1, 1]
product2 = reduce(operator.mul, nums)
print(product2)            # 60

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   lambda x: expr          — anonymous single-expression function
#   map(f, it)              — apply f to every item (lazy)
#   filter(f, it)           — keep items where f returns True (lazy)
#   reduce(f, it, initial)  — fold list into single value
#   operator module         — built-in operator functions
# ─────────────────────────────────────────────
