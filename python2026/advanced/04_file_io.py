# ─────────────────────────────────────────────
# ADV 04 — File I/O
# ─────────────────────────────────────────────
#
# WHAT IS FILE I/O?
#   File I/O (Input/Output) means reading from or writing to
#   files on disk. Programs often need to save data between
#   runs, load configuration, or export results.
#   Python's built-in open() function handles text and binary
#   files. Always use a 'with' block — it guarantees the file
#   is closed even if an error occurs.
# ─────────────────────────────────────────────

import os
import json
import csv

DEMO_FILE = "/tmp/py2026_demo.txt"
JSON_FILE = "/tmp/py2026_data.json"
CSV_FILE  = "/tmp/py2026_data.csv"

# ── 1. Writing a text file ────────────────────

# "w" = write (creates or overwrites)
with open(DEMO_FILE, "w") as f:
    f.write("Line 1: Hello, File!\n")
    f.write("Line 2: Python is great.\n")
    f.write("Line 3: Always use context managers.\n")

# writelines() — write a list of strings (no auto newline)
with open(DEMO_FILE, "a") as f:   # "a" = append
    lines = ["Line 4: Appended later.\n", "Line 5: The end.\n"]
    f.writelines(lines)

# ── 2. Reading a text file ────────────────────

# Read entire file at once
with open(DEMO_FILE, "r") as f:
    content = f.read()
print(content)

# Read line by line (memory-efficient for large files)
with open(DEMO_FILE, "r") as f:
    for line in f:
        print(line, end="")     # line already has \n

# Read all lines into a list
with open(DEMO_FILE, "r") as f:
    lines = f.readlines()
print(lines[0].strip())         # Line 1: Hello, File!

# Read one line at a time
with open(DEMO_FILE, "r") as f:
    first  = f.readline()       # reads first line
    second = f.readline()       # reads second line
print(first.strip(), second.strip())

# ── 3. File modes ─────────────────────────────
# "r"   — read text (default)
# "w"   — write text (create / overwrite)
# "a"   — append text
# "x"   — exclusive creation (fails if file exists)
# "rb"  — read binary
# "wb"  — write binary
# "r+"  — read AND write (no truncate)
# "w+"  — read AND write (truncate)

# ── 4. File path helpers ──────────────────────
print(os.path.exists(DEMO_FILE))            # True
print(os.path.getsize(DEMO_FILE))           # size in bytes
print(os.path.dirname(DEMO_FILE))           # /tmp
print(os.path.basename(DEMO_FILE))          # py2026_demo.txt
name, ext = os.path.splitext("report.pdf")  # ('report', '.pdf')

# List files in a directory
for entry in os.listdir("/tmp"):
    if entry.startswith("py2026"):
        print(entry)

# ── 5. JSON files ─────────────────────────────
data = {
    "students": [
        {"name": "Alice", "score": 92},
        {"name": "Bob",   "score": 85},
    ],
    "course": "Python 2026"
}

# Write JSON
with open(JSON_FILE, "w") as f:
    json.dump(data, f, indent=2)

# Read JSON
with open(JSON_FILE, "r") as f:
    loaded = json.load(f)

print(loaded["course"])                     # Python 2026
print(loaded["students"][0]["name"])        # Alice

# ── 6. CSV files ───────────────────────────────
rows = [
    ["Name", "Age", "City"],
    ["Alice", 30, "Nairobi"],
    ["Bob",   25, "London"],
    ["Carol", 35, "Toronto"],
]

# Write CSV
with open(CSV_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# Read CSV
with open(CSV_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# DictReader — each row as a dict
with open(CSV_FILE, "r") as f:
    for person in csv.DictReader(f):
        print(person["Name"], person["City"])

# ── 7. pathlib (modern path handling, Python 3.4+) ──
from pathlib import Path

p = Path("/tmp")
demo = p / "py2026_pathlib.txt"           # / operator builds paths

demo.write_text("Written via pathlib!\n")
print(demo.read_text())

print(demo.name)          # py2026_pathlib.txt
print(demo.suffix)        # .txt
print(demo.parent)        # /tmp
print(demo.exists())      # True
print(demo.stat().st_size)  # size in bytes

# Glob — find all .txt files in /tmp
for f in p.glob("py2026*.txt"):
    print(f)

# Cleanup demo files
for path in [DEMO_FILE, JSON_FILE, CSV_FILE, str(demo)]:
    if os.path.exists(path):
        os.remove(path)

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   open(file, mode)         — open a file (always use with)
#   read / readline / readlines / write / writelines
#   json.dump / json.load    — read-write JSON
#   csv.writer / DictReader  — read-write CSV
#   pathlib.Path             — modern, OO path handling
# ─────────────────────────────────────────────
