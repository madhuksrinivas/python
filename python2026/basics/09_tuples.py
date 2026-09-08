# ─────────────────────────────────────────────
# 09 — Tuples
# ─────────────────────────────────────────────
#
# WHAT IS A TUPLE?
#   A tuple is an ordered, immutable (unchangeable) collection
#   of items. Once created, you cannot add, remove, or change
#   its elements. Tuples are defined with parentheses: (1, 2, 3)
#   Use a tuple when the data should not change — e.g. coordinates,
#   RGB colours, or returning multiple values from a function.
# ─────────────────────────────────────────────

# --- Creating tuples ---
empty    = ()
single   = (42,)          # trailing comma makes it a tuple, not just (42)
coords   = (10, 20)
rgb      = (255, 128, 0)
mixed    = (1, "hello", 3.14, True)
no_parens = 1, 2, 3       # parentheses are optional

print(type(single))       # <class 'tuple'>
print(type((42)))         # <class 'int'>  — NOT a tuple!

# --- Indexing & slicing (same as lists) ---
point = (4, 7, 9)
print(point[0])           # 4
print(point[-1])          # 9
print(point[1:])          # (7, 9)

# --- Tuples are IMMUTABLE ---
# point[0] = 99  → TypeError: 'tuple' object does not support item assignment
# You must create a new tuple to "change" a value.
new_point = (99,) + point[1:]
print(new_point)          # (99, 7, 9)

# --- Tuple methods (only two) ---
nums = (1, 2, 2, 3, 4, 2)
print(nums.count(2))      # 3
print(nums.index(3))      # 3  (first index of value 3)

# --- Packing & unpacking ---
person = ("Alice", 30, "Engineer")    # packing

name, age, job = person               # unpacking
print(name, age, job)

# Swap variables using tuple unpacking
a, b = 5, 10
a, b = b, a
print(a, b)               # 10 5

# Extended unpacking
first, *middle, last = (1, 2, 3, 4, 5)
print(first, middle, last)   # 1 [2, 3, 4] 5

# --- Named tuples — tuples with labels ---
from collections import namedtuple

Point   = namedtuple("Point",   ["x", "y"])
Student = namedtuple("Student", ["name", "grade", "age"])

p = Point(3, 7)
print(p.x, p.y)           # 3 7
print(p[0])               # 3  (still index-able)

s = Student("Bob", "A", 20)
print(s.name, s.grade)    # Bob A

# --- Why use tuples? ---
# 1. Immutability prevents accidental changes.
# 2. Tuples are faster than lists for iteration.
# 3. Can be used as dictionary keys (lists cannot).
# 4. Convey "this shouldn't change" to other developers.

# Tuple as dict key (lists would raise TypeError)
locations = {(0, 0): "origin", (1, 0): "x-axis", (0, 1): "y-axis"}
print(locations[(1, 0)])  # x-axis

# --- Converting between list and tuple ---
my_list  = [1, 2, 3]
my_tuple = tuple(my_list)
back     = list(my_tuple)
print(my_tuple)   # (1, 2, 3)
print(back)       # [1, 2, 3]

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   ()  vs  (x,)        — tuple vs single-element tuple
#   Immutable           — cannot change after creation
#   Packing/unpacking   — a, b = (1, 2)
#   namedtuple          — tuple with named fields
#   Usable as dict keys — unlike lists
# ─────────────────────────────────────────────
