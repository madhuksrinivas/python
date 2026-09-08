# ─────────────────────────────────────────────
# 06 — Conditionals (if / elif / else)
# ─────────────────────────────────────────────
#
# WHAT ARE CONDITIONALS?
#   Conditionals let your program make decisions.
#   "If this is true, do A; otherwise do B."
#   Python uses if / elif / else blocks.
#   Indentation (4 spaces) defines which code belongs
#   to each branch — there are no curly braces.
# ─────────────────────────────────────────────

# --- Basic if ---
temperature = 35

if temperature > 30:
    print("It's hot!")          # runs: temperature is 35

# --- if / else ---
age = 17

if age >= 18:
    print("You can vote.")
else:
    print("Too young to vote.")  # runs

# --- if / elif / else ---
score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score {score} → Grade {grade}")   # Score 75 → Grade C

# --- Nested if ---
x = 15

if x > 0:
    if x % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")    # runs
else:
    print("Non-positive")

# --- Ternary (one-liner conditional) ---
n = 7
label = "odd" if n % 2 != 0 else "even"
print(label)       # odd

# --- Truthy / Falsy values ---
# Falsy: 0, 0.0, "", [], {}, set(), None, False
# Everything else is truthy.

value = []
if not value:
    print("Empty list is falsy")   # runs

value = [1, 2]
if value:
    print("Non-empty list is truthy")  # runs

# --- Chained comparisons (Python only!) ---
x = 5
print(1 < x < 10)    # True  — equivalent to (1 < x) and (x < 10)
print(1 < x < 4)     # False

# --- Match statement (Python 3.10+) ─────────
command = "quit"

match command:
    case "start":
        print("Starting…")
    case "stop" | "quit":
        print("Stopping…")    # runs
    case _:                   # default / wildcard
        print("Unknown command")

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   if / elif / else    — control flow branching
#   value if cond else  — ternary expression
#   Truthy/Falsy        — implicit boolean evaluation
#   match/case          — pattern matching (3.10+)
#   1 < x < 10          — chained comparison
# ─────────────────────────────────────────────
