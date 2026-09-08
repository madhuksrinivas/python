# ─────────────────────────────────────────────
# 08 — Lists
# ─────────────────────────────────────────────
#
# WHAT IS A LIST?
#   A list is an ordered, mutable (changeable) collection
#   of items. Items can be of any type and can be duplicated.
#   Lists are defined with square brackets: [1, 2, 3]
#   They are the most commonly used data structure in Python.
# ─────────────────────────────────────────────

# --- Creating a list ---
empty   = []
numbers = [1, 2, 3, 4, 5]
mixed   = [1, "hello", 3.14, True, None]
nested  = [[1, 2], [3, 4], [5, 6]]

# --- Indexing & slicing (same as strings) ---
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[0])        # apple
print(fruits[-1])       # elderberry
print(fruits[1:3])      # ['banana', 'cherry']
print(fruits[::-1])     # reversed list

# --- Modifying elements ---
fruits[1] = "blueberry"
print(fruits)           # ['apple', 'blueberry', 'cherry', 'date', 'elderberry']

# --- Adding elements ---
fruits.append("fig")            # add to end
fruits.insert(1, "avocado")     # insert at index
fruits.extend(["grape", "kiwi"])  # add multiple items
print(fruits)

# --- Removing elements ---
fruits.remove("date")           # remove first occurrence by value
popped = fruits.pop()           # remove & return last item
popped2 = fruits.pop(0)         # remove & return item at index 0
del fruits[0]                   # delete by index (no return)
print(popped, popped2)

# --- Searching ---
nums = [10, 20, 30, 20, 40]
print(20 in nums)               # True
print(nums.index(20))           # 1  (first occurrence)
print(nums.count(20))           # 2

# --- Sorting ---
nums.sort()                     # sort in place (ascending)
print(nums)                     # [10, 20, 20, 30, 40]

nums.sort(reverse=True)
print(nums)                     # [40, 30, 20, 20, 10]

words = ["banana", "apple", "cherry"]
words.sort(key=len)             # sort by string length
print(words)                    # ['apple', 'banana', 'cherry']

sorted_copy = sorted(words)     # returns NEW sorted list, original unchanged
print(sorted_copy)

nums.reverse()                  # reverse in place
print(nums)

# --- Other useful methods ---
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(len(nums))                # 8
print(min(nums), max(nums))     # 1 9
print(sum(nums))                # 31

nums.clear()                    # empty the list
print(nums)                     # []

# --- Copying a list ---
original = [1, 2, 3]
shallow  = original.copy()      # or list(original) or original[:]
shallow.append(4)
print(original)                 # [1, 2, 3]  — not affected
print(shallow)                  # [1, 2, 3, 4]

# --- Nested lists ---
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix[1][2])             # 6  (row 1, column 2)

for row in matrix:
    print(row)

# --- List unpacking ---
a, b, c = [10, 20, 30]
print(a, b, c)                  # 10 20 30

first, *rest = [1, 2, 3, 4, 5]
print(first, rest)              # 1  [2, 3, 4, 5]

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   append, insert, extend   — adding items
#   remove, pop, del         — removing items
#   sort(key=…), sorted()    — sorting
#   copy() / [:]             — shallow copy
#   * unpacking              — spread into rest
# ─────────────────────────────────────────────
