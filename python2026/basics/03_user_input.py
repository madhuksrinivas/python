# ─────────────────────────────────────────────
# 03 — User Input & Output
# ─────────────────────────────────────────────
#
# WHAT IS USER INPUT?
#   Programs become interactive when they can ask the user
#   for information while running. Python's built-in input()
#   function pauses the program, shows a prompt, waits for
#   the user to type something, and returns it as a string.
# ─────────────────────────────────────────────

# input() always returns a STRING
name = input("What is your name? ")
print("Hello,", name)

# Convert input to a number before doing math
age = int(input("How old are you? "))
print("Next year you will be", age + 1)

height = float(input("Your height in meters: "))
print(f"Height doubled: {height * 2:.2f} m")

# --- Formatted output (f-strings — preferred since Python 3.6) ---
city = "Nairobi"
temp = 28.5
print(f"It is {temp}°C in {city}.")       # It is 28.5°C in Nairobi.

# Number formatting inside f-strings
pi = 3.14159265
print(f"Pi to 2 decimal places: {pi:.2f}")  # 3.14
print(f"Large number: {1_000_000:,}")        # 1,000,000

# Older style (still valid)
print("Name: %s, Age: %d" % ("Bob", 30))    # Name: Bob, Age: 30
print("Name: {}, Age: {}".format("Bob", 30))

# --- Multiline input trick ---
# Uncomment to try:
# lines = []
# print("Enter 3 lines:")
# for _ in range(3):
#     lines.append(input())
# print("You entered:", lines)

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   input()       — reads a line from the user (always str)
#   int/float()   — cast input to a number
#   f-strings     — f"Hello {variable}"  (fast + readable)
#   :.2f          — format float to 2 decimal places
#   :,            — add thousands separator
# ─────────────────────────────────────────────
