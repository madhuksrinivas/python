# ─────────────────────────────────────────────
# 12 — Functions
# ─────────────────────────────────────────────
#
# WHAT IS A FUNCTION?
#   A function is a reusable block of code that does one job.
#   You define it once with 'def' and call it as many times
#   as you like. Functions can accept inputs (parameters) and
#   send back a result (return value). They are the foundation
#   of clean, non-repetitive code.
# ─────────────────────────────────────────────

# --- Defining and calling ---
def greet():
    print("Hello!")

greet()    # Hello!

# --- Parameters & return value ---
def add(a, b):
    return a + b

result = add(3, 7)
print(result)    # 10

# --- Default parameter values ---
def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet_user("Alice")              # Hello, Alice!
greet_user("Bob", "Good morning")  # Good morning, Bob!

# --- Keyword arguments (order doesn't matter) ---
def describe(name, age, city):
    print(f"{name}, {age}, from {city}")

describe(age=30, city="Nairobi", name="Alice")

# --- *args — variable number of positional args ---
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3))        # 6
print(total(10, 20, 30, 40)) # 100

# --- **kwargs — variable number of keyword args ---
def display_info(**details):
    for key, value in details.items():
        print(f"  {key}: {value}")

display_info(name="Alice", age=30, job="Developer")

# --- Combining all parameter types ---
# Order: positional → *args → keyword-only → **kwargs
def mixed(a, b, *args, sep=", ", **kwargs):
    print(a, b, args, sep, kwargs)

mixed(1, 2, 3, 4, sep="-", x=10, y=20)
# 1 2 (3, 4) - {'x': 10, 'y': 20}

# --- Returning multiple values (returns a tuple) ---
def min_max(numbers):
    return min(numbers), max(numbers)

lo, hi = min_max([5, 3, 8, 1, 9])
print(lo, hi)    # 1 9

# --- Functions are first-class objects ---
def square(n):
    return n * n

func = square           # assign function to variable
print(func(5))          # 25

ops = [abs, square, str]
for op in ops:
    print(op(-4))       # 4, 16, '-4'

# --- Passing functions as arguments ---
def apply(func, value):
    return func(value)

print(apply(square, 6))    # 36

# --- Scope: LEGB rule ---
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)        # local
    inner()
    print(x)            # enclosing

outer()
print(x)                # global

# --- global keyword ---
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(counter)    # 2

# --- Docstrings ---
def multiply(a, b):
    """Return the product of a and b."""
    return a * b

print(multiply.__doc__)    # Return the product of a and b.
help(multiply)             # shows docstring in terminal

# --- Recursion ---
def factorial(n):
    if n <= 1:           # base case
        return 1
    return n * factorial(n - 1)

print(factorial(5))    # 120  (5*4*3*2*1)

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   def / return         — define a function
#   default params       — greet(name, greeting="Hi")
#   *args / **kwargs     — flexible argument lists
#   LEGB scope           — Local → Enclosing → Global → Built-in
#   global keyword       — modify a global variable
#   Recursion            — function calling itself
# ─────────────────────────────────────────────
