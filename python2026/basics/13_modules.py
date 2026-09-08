# ─────────────────────────────────────────────
# 13 — Modules & Packages
# ─────────────────────────────────────────────
#
# WHAT IS A MODULE?
#   A module is simply a .py file that contains code you want
#   to reuse. Python ships with hundreds of built-in modules
#   (the "standard library") — for maths, dates, files, etc.
#
# WHAT IS A PACKAGE?
#   A package is a folder of modules that share a related purpose.
#   Third-party packages (like numpy, requests) are installed
#   via pip: pip install <package-name>
# ─────────────────────────────────────────────

# --- Importing standard library modules ---
import math
import random
import os
import sys
import datetime

# math
print(math.pi)                    # 3.141592653589793
print(math.sqrt(144))             # 12.0
print(math.ceil(4.2))             # 5
print(math.floor(4.9))            # 4
print(math.log(100, 10))          # 2.0

# random
random.seed(42)                   # reproducible results
print(random.randint(1, 10))      # random int 1–10
print(random.choice(["a","b","c"]))  # random item
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)
print(random.sample(items, 3))    # 3 unique random items

# os
print(os.getcwd())                # current working directory
print(os.path.join("folder", "file.txt"))  # cross-platform path
print(os.path.exists("/tmp"))     # True / False
print(os.path.basename("/usr/local/bin/python"))  # python

# datetime
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))   # e.g. 2026-08-20 14:30:00
today = datetime.date.today()
print(today.year, today.month, today.day)

delta = datetime.timedelta(days=7)
print(today + delta)   # one week from today

# sys
print(sys.version)     # Python version string
print(sys.platform)    # 'darwin', 'linux', 'win32'

# --- Import specific names ---
from math import pi, sqrt, pow as math_pow
print(pi)              # 3.141592...
print(sqrt(25))        # 5.0

# --- Import with alias ---
import numpy as np              # common convention
# (numpy must be installed: pip install numpy)
# arr = np.array([1, 2, 3])

import json
data = {"name": "Alice", "scores": [90, 85, 92]}
json_str = json.dumps(data, indent=2)   # dict → JSON string
print(json_str)
back = json.loads(json_str)             # JSON string → dict
print(back["name"])                     # Alice

# --- Creating your own module ---
# Imagine you have a file  mymath.py  with:
#
#   def add(a, b):
#       return a + b
#
#   def multiply(a, b):
#       return a * b
#
#   PI = 3.14159
#
# Then in another file:
#   import mymath
#   print(mymath.add(2, 3))      # 5
#   print(mymath.PI)             # 3.14159
#
#   from mymath import multiply
#   print(multiply(4, 5))        # 20

# --- __name__ guard ---
# Every module has __name__:
#   - when run directly   →  __name__ == "__main__"
#   - when imported       →  __name__ == "mymath" (the module name)
#
# This lets you have code that only runs when the file is executed directly:

def main():
    print("Running as main script")

if __name__ == "__main__":
    main()

# --- Packages ---
# A package is a folder containing an __init__.py file (can be empty).
#
# mypackage/
#   __init__.py
#   utils.py
#   models.py
#
# Usage:
#   from mypackage import utils
#   from mypackage.models import User

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   import module              — import whole module
#   from module import name    — import specific item
#   import module as alias     — rename on import
#   __name__ == "__main__"     — run-if-main guard
#   Package = folder + __init__.py
# ─────────────────────────────────────────────
