# ─────────────────────────────────────────────
# 14 — Error Handling (Exceptions)
# ─────────────────────────────────────────────
#
# WHAT IS AN EXCEPTION?
#   An exception is an error that occurs while the program
#   is running — dividing by zero, opening a missing file,
#   using the wrong type, etc. Without handling them the
#   program crashes. Python's try/except block lets you
#   catch an error and decide what to do instead of crashing.
# ─────────────────────────────────────────────

# --- Basic try / except ---
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")     # runs

# --- Catching multiple exception types ---
def parse_number(s):
    try:
        return int(s)
    except ValueError:
        print(f"'{s}' is not a valid integer")
    except TypeError:
        print("Expected a string, got something else")

parse_number("42")      # 42 (no error)
parse_number("abc")     # ValueError caught
parse_number(None)      # TypeError caught

# --- except with the exception object ---
try:
    nums = [1, 2, 3]
    print(nums[10])
except IndexError as e:
    print(f"IndexError: {e}")    # list index out of range

# --- Catching multiple exceptions in one line ---
try:
    x = int(input("Enter a number (or letters): "))
    print(100 / x)
except (ValueError, ZeroDivisionError) as e:
    print(f"Handled: {e}")

# --- else — runs only if NO exception occurred ---
try:
    n = int("99")
except ValueError:
    print("Bad input")
else:
    print(f"Parsed successfully: {n}")   # runs

# --- finally — ALWAYS runs (cleanup code) ---
try:
    f = open("/tmp/test_py2026.txt", "w")
    f.write("hello")
    result = 1 / 0           # triggers exception
except ZeroDivisionError:
    print("Division error")
finally:
    f.close()                # always closes the file
    print("File closed")

# --- Raising exceptions ---
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0 or age > 150:
        raise ValueError(f"Age {age} is out of range")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(e)   # Age -5 is out of range

# --- Custom exception classes ---
class InsufficientFundsError(Exception):
    """Raised when a bank withdrawal exceeds the balance."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount  = amount
        super().__init__(f"Cannot withdraw {amount}; balance is {balance}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(e)    # Cannot withdraw 150; balance is 100

# --- assert — quick sanity checks ---
def divide(a, b):
    assert b != 0, "Denominator must not be zero"
    return a / b

try:
    divide(10, 0)
except AssertionError as e:
    print(e)    # Denominator must not be zero

# --- Common built-in exceptions ---
# ValueError       — wrong value  (int("abc"))
# TypeError        — wrong type   (1 + "a")
# KeyError         — missing dict key
# IndexError       — list index out of range
# AttributeError   — object has no such attribute
# FileNotFoundError — file doesn't exist
# ZeroDivisionError — dividing by zero
# OverflowError    — number too large
# ImportError      — module not found
# PermissionError  — OS permission denied
# RuntimeError     — generic runtime problem
# StopIteration    — iterator exhausted

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   try / except / else / finally
#   raise ExceptionType("message")
#   Custom exceptions — subclass Exception
#   assert condition, "message"
# ─────────────────────────────────────────────
