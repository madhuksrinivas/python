# ─────────────────────────────────────────────
# 05 — Strings
# ─────────────────────────────────────────────
#
# WHAT IS A STRING?
#   A string is a sequence of characters enclosed in quotes.
#   Strings are immutable — you cannot change a character in
#   place; you always create a new string.
#   Python strings come with dozens of built-in methods for
#   searching, replacing, splitting, and formatting text.
# ─────────────────────────────────────────────

# --- Creation ---
s1 = "double quotes"
s2 = 'single quotes'
s3 = """Triple quotes
span multiple lines"""

# --- Concatenation & repetition ---
greeting = "Hello" + ", " + "World!"   # Hello, World!
laugh = "ha" * 3                        # hahaha
print(greeting, laugh)

# --- Indexing & slicing ---
word = "Python"
print(word[0])      # P   (0-based, positive)
print(word[-1])     # n   (negative index from end)
print(word[1:4])    # yth (start:stop, stop excluded)
print(word[:3])     # Pyt (from beginning)
print(word[3:])     # hon (to end)
print(word[::2])    # Pto (every 2nd character)
print(word[::-1])   # nohtyP (reverse)

# --- Common string methods ---
msg = "  hello, python world!  "

print(msg.strip())          # remove leading/trailing spaces
print(msg.upper())          # HELLO, PYTHON WORLD!
print(msg.lower())          # (already lowercase)
print(msg.title())          #   Hello, Python World!
print(msg.replace("python", "amazing"))
print(msg.split(","))       # ['  hello', ' python world!  ']
print(",".join(["a", "b", "c"]))  # a,b,c

# Check methods
print("hello".startswith("he"))   # True
print("hello".endswith("lo"))     # True
print("hello".isalpha())          # True (all letters)
print("123".isdigit())            # True
print("  ".isspace())             # True
print("hello".find("ll"))         # 2  (index of first match)
print("hello".count("l"))         # 2

# --- f-strings (formatted string literals) ---
name  = "Alice"
score = 98.6
print(f"{name} scored {score:.1f}%")    # Alice scored 98.6%
print(f"{'centered':^20}")              #       centered
print(f"{'left':<20}|")                 # left                |
print(f"{'right':>20}|")                #                right|
print(f"{1000000:,}")                   # 1,000,000
print(f"{255:#010b}")                   # 0b11111111 (binary)

# --- Escape sequences ---
print("Quotes: \"double\" and \'single\'")
print("Backslash: \\")
print("Tab:\there")
print("Unicode heart: \u2665")

# --- len and in ---
sentence = "The quick brown fox"
print(len(sentence))                # 19
print("quick" in sentence)          # True
print("slow"  not in sentence)      # True

# --- Strings are immutable ---
# word[0] = "J"  → TypeError!
# Use replace or re-assignment instead.
word = "J" + word[1:]
print(word)    # Jython

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   [start:stop:step]  — slicing
#   strip, split, join, replace, find, count  — key methods
#   f-strings with format specs  :.2f  :>20  :,
#   Strings are immutable sequences
# ─────────────────────────────────────────────
