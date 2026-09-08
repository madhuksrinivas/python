# ─────────────────────────────────────────────
# ADV 05 — Decorators
# ─────────────────────────────────────────────
#
# WHAT IS A DECORATOR?
#   A decorator is a function that wraps another function to
#   add extra behaviour (logging, timing, caching, auth checks)
#   without changing the original function's code.
#   The @syntax is shorthand for: my_func = decorator(my_func)
#   You'll find decorators everywhere in real Python projects
#   — Flask routes, Django views, FastAPI endpoints, etc.
# ─────────────────────────────────────────────

import time
import functools

# ── Background: functions are first-class ────
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(func, message):       # functions passed as arguments
    return func(message)

print(speak(shout,   "hello"))  # HELLO
print(speak(whisper, "HELLO"))  # hello


# ── Functions returning functions (closures) ─
def make_multiplier(n):
    def multiplier(x):
        return x * n           # "closes over" n
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))               # 10
print(triple(5))               # 15


# ── 1. Basic decorator ───────────────────────
# A decorator is a function that wraps another function.

def my_decorator(func):
    @functools.wraps(func)      # preserve original function's metadata
    def wrapper(*args, **kwargs):
        print("Before the function")
        result = func(*args, **kwargs)
        print("After the function")
        return result
    return wrapper

@my_decorator                   # equivalent to: greet = my_decorator(greet)
def greet(name):
    """Greet someone by name."""
    print(f"Hello, {name}!")

greet("Alice")
# Before the function
# Hello, Alice!
# After the function
print(greet.__name__)           # greet  (preserved by @functools.wraps)


# ── 2. Timing decorator ──────────────────────
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start  = time.perf_counter()
        result = func(*args, **kwargs)
        end    = time.perf_counter()
        print(f"{func.__name__} ran in {end - start:.6f} seconds")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

print(slow_sum(1_000_000))


# ── 3. Logging decorator ─────────────────────
def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}(args={args}, kwargs={kwargs})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

add(3, 7)
# Calling add(args=(3, 7), kwargs={})
# add returned 10


# ── 4. Decorator with arguments ──────────────
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hi():
    print("Hi!")

say_hi()    # Hi! (×3)


# ── 5. Stacking decorators ───────────────────
@timer
@log_calls
def multiply(a, b):
    return a * b

multiply(6, 7)
# Applied bottom-up: log_calls wraps multiply first, then timer wraps that


# ── 6. Class-based decorator ─────────────────
class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func  = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call #{self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def hello():
    print("Hello!")

hello()    # Call #1 to hello / Hello!
hello()    # Call #2 to hello / Hello!
print(hello.count)   # 2


# ── 7. @property (built-in decorator) ───────
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32


t = Temperature(25)
print(t.fahrenheit)    # 77.0
t.celsius = 100
print(t.fahrenheit)    # 212.0


# ── Common built-in decorators ───────────────
# @property          — getter / setter for attributes
# @staticmethod      — method with no self or cls
# @classmethod       — method receiving cls
# @functools.cache   — memoize return values
# @functools.lru_cache(maxsize=128) — LRU cache

from functools import cache

@cache
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(50))    # instant even for large n

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   Decorator = function wrapping another function
#   @functools.wraps  — preserve __name__, __doc__
#   Decorator with args — use 3 levels of nesting
#   Stacking — applied bottom-up
#   @cache            — automatic memoization
# ─────────────────────────────────────────────
