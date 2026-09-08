# ─────────────────────────────────────────────
# 04 — Operators
# ─────────────────────────────────────────────
#
# WHAT ARE OPERATORS?
#   Operators are special symbols that perform operations on values.
#   Python has several groups:
#     Arithmetic   — + - * / // % **
#     Comparison   — == != > < >= <=
#     Logical      — and, or, not
#     Assignment   — = += -= *= etc.
#     Membership   — in, not in
#     Identity     — is, is not
#     Bitwise      — & | ^ ~ << >>
# ─────────────────────────────────────────────

# ── Arithmetic ──────────────────────────────
print(10 + 3)    # 13  addition
print(10 - 3)    # 7   subtraction
print(10 * 3)    # 30  multiplication
print(10 / 3)    # 3.3333...  true division (always float)
print(10 // 3)   # 3   floor division (integer result)
print(10 % 3)    # 1   modulus (remainder)
print(2 ** 8)    # 256 exponentiation

# ── Comparison (return True / False) ────────
print(5 == 5)    # True
print(5 != 4)    # True
print(7 > 3)     # True
print(7 < 3)     # False
print(5 >= 5)    # True
print(5 <= 4)    # False

# ── Logical ─────────────────────────────────
print(True and False)   # False — both must be True
print(True or False)    # True  — at least one True
print(not True)         # False

# Short-circuit evaluation
x = 0
print(x != 0 and 10 / x > 1)  # False — right side never evaluated

# ── Assignment shortcuts ─────────────────────
n = 10
n += 3;  print(n)   # 13
n -= 2;  print(n)   # 11
n *= 2;  print(n)   # 22
n //= 3; print(n)   # 7
n **= 2; print(n)   # 49
n %= 10; print(n)   # 9

# ── Membership & Identity ────────────────────
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)        # True
print("grape" not in fruits)    # True

a = [1, 2, 3]
b = a              # b points to the same list
c = [1, 2, 3]      # c is a different list with same values
print(a is b)      # True  — same object
print(a is c)      # False — different objects
print(a == c)      # True  — same values

# ── Bitwise (integers as bits) ───────────────
print(0b1010 & 0b1100)   # 8   AND
print(0b1010 | 0b1100)   # 14  OR
print(0b1010 ^ 0b1100)   # 6   XOR
print(~0b1010)            # -11 NOT
print(1 << 3)             # 8   left shift
print(16 >> 2)            # 4   right shift

# ── Operator precedence (high → low) ─────────
# ** → unary +/- → * / // % → + - → comparisons → not → and → or
result = 2 + 3 * 4 ** 2 - 1   # 2 + 3*16 - 1 = 49
print(result)

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   // %       — floor division and modulus
#   **         — power
#   and or not — logical operators
#   is / in    — identity and membership tests
# ─────────────────────────────────────────────
