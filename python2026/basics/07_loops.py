# ─────────────────────────────────────────────
# 07 — Loops  (for, while, break, continue, else)
# ─────────────────────────────────────────────
#
# WHAT IS A LOOP?
#   A loop repeats a block of code multiple times so you
#   don't have to write the same thing over and over.
#   Python has two kinds:
#     for   — iterate over a sequence (list, string, range…)
#     while — keep running as long as a condition is True
# ─────────────────────────────────────────────

# ── for loop over a list ─────────────────────
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# apple
# banana
# cherry

# ── range() ──────────────────────────────────
for i in range(5):          # 0 1 2 3 4
    print(i, end=" ")
print()

for i in range(2, 10, 2):   # 2 4 6 8  (start, stop, step)
    print(i, end=" ")
print()

for i in range(10, 0, -1):  # 10 down to 1
    print(i, end=" ")
print()

# ── enumerate() — index + value ──────────────
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
# 1. apple
# 2. banana
# 3. cherry

# ── zip() — loop two lists together ──────────
names  = ["Alice", "Bob", "Carol"]
scores = [90, 85, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# ── Iterating a string ────────────────────────
for char in "Hello":
    print(char, end="-")    # H-e-l-l-o-
print()

# ── while loop ───────────────────────────────
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
print()                     # 0 1 2 3 4

# ── break — exit the loop early ──────────────
for n in range(10):
    if n == 5:
        break
    print(n, end=" ")       # 0 1 2 3 4
print()

# ── continue — skip the rest of this iteration
for n in range(10):
    if n % 2 == 0:
        continue            # skip even numbers
    print(n, end=" ")       # 1 3 5 7 9
print()

# ── else on a loop — runs if loop completes normally (no break)
for n in range(5):
    if n == 10:             # never true
        break
else:
    print("Loop finished without break")   # runs

for n in range(5):
    if n == 3:
        break
else:
    print("Never printed — loop was broken")

# ── Nested loops ─────────────────────────────
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row*col:2}", end=" ")
    print()
# multiplication table 3×3

# ── while with break (search pattern) ────────
import random
random.seed(1)
attempts = 0
while True:
    n = random.randint(1, 10)
    attempts += 1
    if n == 7:
        print(f"Found 7 after {attempts} attempts!")
        break

# ── pass — placeholder, does nothing ──────────
for i in range(3):
    pass    # useful while writing skeleton code

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   for … in          — iterate any iterable
#   range(start,stop,step) — number sequence
#   enumerate()       — index + value together
#   zip()             — parallel iteration
#   break / continue  — loop control
#   while True + break — indefinite loop pattern
#   for/while … else  — runs when no break hit
# ─────────────────────────────────────────────
