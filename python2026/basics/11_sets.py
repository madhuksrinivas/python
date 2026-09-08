# ─────────────────────────────────────────────
# 11 — Sets
# ─────────────────────────────────────────────
#
# WHAT IS A SET?
#   A set is an unordered collection of unique items.
#   Duplicates are automatically removed.
#   Sets support mathematical operations like union,
#   intersection, and difference — just like in maths class.
#   Membership checks (in) are O(1) — much faster than lists.
# ─────────────────────────────────────────────

# --- Creating a set ---
# A set is an UNORDERED collection of UNIQUE values.
empty_set = set()           # NOT {} — that creates an empty dict!
fruits = {"apple", "banana", "cherry", "apple"}  # duplicate removed
print(fruits)               # {'apple', 'banana', 'cherry'} (order may vary)
print(type(empty_set))      # <class 'set'>

# From a list (great for removing duplicates)
nums = [1, 2, 2, 3, 4, 4, 4, 5]
unique = set(nums)
print(unique)               # {1, 2, 3, 4, 5}

# --- Adding / removing ---
fruits.add("date")          # add one element
fruits.update(["elderberry", "fig"])  # add multiple

fruits.remove("banana")     # raises KeyError if not found
fruits.discard("grape")     # safe remove — no error if missing
popped = fruits.pop()       # remove & return an arbitrary element
print(popped)

# --- Membership (O(1) — much faster than list!) ---
primes = {2, 3, 5, 7, 11, 13}
print(7 in primes)          # True
print(9 in primes)          # False

# --- Set operations ---
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a | b)                # union        {1,2,3,4,5,6,7,8}
print(a & b)                # intersection {4, 5}
print(a - b)                # difference   {1, 2, 3}
print(a ^ b)                # symmetric difference {1,2,3,6,7,8}

# Equivalent methods
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

# --- Subset / Superset ---
x = {1, 2}
y = {1, 2, 3, 4}
print(x.issubset(y))        # True  — all of x is in y
print(y.issuperset(x))      # True  — y contains all of x
print(x.isdisjoint({5, 6})) # True  — no common elements

# --- In-place operations ---
a |= {9, 10}                # union in place
a &= {1, 2, 9}              # intersection in place
print(a)                    # {1, 2, 9}

# --- Frozenset — immutable set ---
fs = frozenset([1, 2, 3])
# fs.add(4)  → AttributeError
print(fs)                   # frozenset({1, 2, 3})

# Frozensets can be dictionary keys or elements of another set
seen = set()
seen.add(frozenset([1, 2]))
seen.add(frozenset([3, 4]))
print(seen)

# --- Practical example: find duplicates in a list ---
items = ["cat", "dog", "cat", "bird", "dog", "fish"]
seen2  = set()
dupes  = set()
for item in items:
    if item in seen2:
        dupes.add(item)
    seen2.add(item)
print("Duplicates:", dupes)    # {'cat', 'dog'}

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   set()            — create empty set (not {})
#   add / discard    — safe adding/removing
#   | & - ^          — union, intersection, diff, sym-diff
#   in check is O(1) — much faster than list
#   frozenset        — immutable set, hashable
# ─────────────────────────────────────────────
