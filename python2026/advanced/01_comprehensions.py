# ─────────────────────────────────────────────
# ADV 01 — List / Dict / Set Comprehensions
# ─────────────────────────────────────────────
#
# WHAT IS A COMPREHENSION?
#   A comprehension is a compact, one-line way to build a new
#   list, dictionary, or set from an existing iterable.
#   Instead of a for-loop + append, you write the logic inline.
#   They are faster than equivalent loops and considered very
#   Pythonic — you will see them everywhere in Python code.
# ─────────────────────────────────────────────

# --- List comprehension ---
# [expression  for item in iterable  if condition]

squares = [x**2 for x in range(1, 11)]
print(squares)    # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

evens = [x for x in range(20) if x % 2 == 0]
print(evens)      # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

words = ["hello", "world", "python", "rocks"]
upper = [w.upper() for w in words if len(w) > 4]
print(upper)      # ['HELLO', 'WORLD', 'PYTHON']

# Equivalent traditional loop
result = []
for w in words:
    if len(w) > 4:
        result.append(w.upper())
# same output, but comprehension is faster and more concise

# --- Nested list comprehension ---
# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Cartesian product
pairs = [(x, y) for x in [1, 2, 3] for y in ["a", "b"]]
print(pairs)

# --- Conditional expression inside comprehension ---
labels = ["even" if x % 2 == 0 else "odd" for x in range(6)]
print(labels)   # ['even', 'odd', 'even', 'odd', 'even', 'odd']

# --- Dictionary comprehension ---
# {key_expr: value_expr  for item in iterable  if condition}

squares_dict = {n: n**2 for n in range(1, 6)}
print(squares_dict)    # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

names  = ["Alice", "Bob", "Carol"]
scores = [90, 85, 92]
grade_book = {name: score for name, score in zip(names, scores)}
print(grade_book)

# Invert a dictionary
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)    # {1: 'a', 2: 'b', 3: 'c'}

# Filter dict entries
passing = {name: score for name, score in grade_book.items() if score >= 88}
print(passing)     # {'Alice': 90, 'Carol': 92}

# --- Set comprehension ---
unique_lengths = {len(w) for w in words}
print(unique_lengths)    # {5, 6}  (order may vary)

# --- Generator expression (memory-efficient) ---
# Same syntax as list comprehension but uses () instead of []
# Does NOT build the whole list — produces values on demand.
gen = (x**2 for x in range(1_000_000))   # no memory spike
print(next(gen))    # 0
print(next(gen))    # 1

# Useful with sum/max/min — no list ever created
total = sum(x**2 for x in range(1001))
print(total)        # 333833500

# any() / all() with generator — short-circuits immediately
print(any(x > 50 for x in range(100)))   # True
print(all(x >= 0 for x in range(10)))    # True

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   [expr for x in it if cond]  — list comprehension
#   {k: v for …}                — dict comprehension
#   {expr for …}                — set comprehension
#   (expr for …)                — generator expression
#   Nested for clauses          — flatten / cartesian
# ─────────────────────────────────────────────
