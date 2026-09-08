# ─────────────────────────────────────────────
# 01 — Hello World, print(), and Comments
# ─────────────────────────────────────────────
#
# WHAT IS print()?
#   print() is a built-in function that outputs text to the screen.
#   It is the first thing every Python programmer learns — it lets
#   you see what your program is doing.
#
# WHAT ARE COMMENTS?
#   Comments are lines that Python ignores completely.
#   Use them to explain your code to yourself and others.
#   A single-line comment starts with #.
# ─────────────────────────────────────────────

# Single-line comment
print("Hello, World!")          # Output: Hello, World!

# print() can handle multiple values separated by commas
print("Hello", "Python", 2026)  # Output: Hello Python 2026

# Customize separator and end character
print("one", "two", "three", sep=" | ")   # Output: one | two | three
print("no newline", end=" ")
print("same line")                        # Output: no newline same line

# Multi-line string (triple quotes)
print("""
This is
a multi-line
output.
""")

# Printing special characters
print("Tab:\there")        # Output: Tab:    here
print("Newline:\nhere")    # Output: Newline:
                           #         here

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   print()   — outputs text/values to the console
#   #         — single-line comment (ignored by Python)
#   """ """   — multi-line string / docstring
#   \t \n     — escape sequences (tab, newline)
# ─────────────────────────────────────────────
