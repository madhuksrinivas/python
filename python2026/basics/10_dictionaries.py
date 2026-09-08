# ─────────────────────────────────────────────
# 10 — Dictionaries
# ─────────────────────────────────────────────
#
# WHAT IS A DICTIONARY?
#   A dictionary stores data as key–value pairs, like a real
#   dictionary where a word (key) maps to its definition (value).
#   Keys must be unique and immutable (str, int, tuple).
#   Values can be anything. Defined with curly braces: {"name": "Alice"}
#   Lookups are extremely fast (O(1) on average).
# ─────────────────────────────────────────────

# --- Creating ---
empty = {}
person = {"name": "Alice", "age": 30, "city": "Nairobi"}

# Also valid: dict() constructor
config = dict(debug=True, version="1.0", port=8080)

print(person)
print(config)

# --- Accessing values ---
print(person["name"])                 # Alice
print(person.get("age"))             # 30
print(person.get("email", "N/A"))    # N/A  (default if key missing)
# person["email"]  → KeyError!  — use .get() when key may not exist

# --- Modifying ---
person["age"] = 31                   # update existing key
person["email"] = "alice@mail.com"   # add new key
del person["city"]                   # remove a key
print(person)

# --- Checking existence ---
print("name" in person)              # True
print("city" in person)              # False (we deleted it)

# --- Iterating ---
scores = {"Alice": 90, "Bob": 85, "Carol": 92}

for key in scores:                   # iterate keys
    print(key)

for value in scores.values():        # iterate values
    print(value)

for key, value in scores.items():    # iterate key-value pairs
    print(f"{key}: {value}")

# --- pop() and popitem() ---
removed = scores.pop("Bob")         # remove key, return value
print(removed)                      # 85

last_pair = scores.popitem()        # remove & return last inserted pair
print(last_pair)                    # ('Carol', 92)

# --- update() — merge another dict ---
defaults = {"theme": "dark", "lang": "en", "debug": False}
overrides = {"lang": "fr", "debug": True}
defaults.update(overrides)
print(defaults)   # {'theme': 'dark', 'lang': 'fr', 'debug': True}

# --- setdefault() — add key only if not present ---
person.setdefault("role", "user")    # adds role = user
person.setdefault("email", "other") # email already exists, no change
print(person["role"])                # user

# --- Nested dictionaries ---
students = {
    "alice": {"grade": "A", "score": 95},
    "bob":   {"grade": "B", "score": 82},
}
print(students["alice"]["score"])    # 95
students["carol"] = {"grade": "A", "score": 91}

# --- Dictionary comprehension (preview) ---
squares = {n: n**2 for n in range(1, 6)}
print(squares)    # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# --- Merge dicts (Python 3.9+) ---
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3}
merged = d1 | d2           # d2 values win on clash
print(merged)              # {'a': 1, 'b': 99, 'c': 3}

# --- Useful methods ---
info = {"x": 1, "y": 2, "z": 3}
print(list(info.keys()))     # ['x', 'y', 'z']
print(list(info.values()))   # [1, 2, 3]
print(list(info.items()))    # [('x', 1), ('y', 2), ('z', 3)]
print(len(info))             # 3

info.clear()
print(info)                  # {}

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   {key: value}          — dict literal
#   .get(key, default)    — safe access
#   .update()             — merge / override
#   .items() .keys() .values() — iteration views
#   d1 | d2               — merge operator (3.9+)
#   Dict comprehension    — {k: v for …}
# ─────────────────────────────────────────────
