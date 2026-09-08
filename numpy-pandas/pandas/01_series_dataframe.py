# ─────────────────────────────────────────────
# PANDAS 01 — Series & DataFrame Basics
# ─────────────────────────────────────────────
#
# WHAT IS PANDAS?
#   Pandas is Python's most important data manipulation library.
#   It provides two core structures:
#     Series    — a labelled 1D array (like a spreadsheet column)
#     DataFrame — a labelled 2D table (like a spreadsheet or SQL table)
#   Every data science pipeline — from raw CSV to model features —
#   passes through Pandas. Install: pip install pandas
# ─────────────────────────────────────────────

import pandas as pd
import numpy as np

print("Pandas version:", pd.__version__)

# ── 1. Series ────────────────────────────────
# A Series is a 1D array with an index (labels).
s = pd.Series([10, 20, 30, 40, 50])
print(s)
# 0    10
# 1    20
# dtype: int64

# Custom index
temps = pd.Series([28.5, 31.0, 25.3, 29.8],
                   index=["Mon", "Tue", "Wed", "Thu"])
print(temps["Tue"])        # 31.0
print(temps[temps > 28])   # filter: Mon and Thu

# Arithmetic on Series (broadcasts like NumPy)
print(temps + 1.5)         # all temps + 1.5

# ── 2. DataFrame creation ────────────────────
# From a dictionary of lists (most common)
df = pd.DataFrame({
    "name":    ["Alice", "Bob", "Carol", "David", "Eve"],
    "age":     [25, 30, 35, 28, 22],
    "city":    ["Nairobi", "London", "Paris", "Nairobi", "Berlin"],
    "salary":  [55000, 72000, 88000, 61000, 49000],
    "active":  [True, True, False, True, False],
})
print(df)
print(df.shape)     # (5, 5)
print(df.dtypes)
print(df.columns.tolist())

# From a list of dicts
records = [{"x": 1, "y": 2}, {"x": 3, "y": 4}]
print(pd.DataFrame(records))

# From a NumPy array
arr = np.random.randint(0, 100, (4, 3))
print(pd.DataFrame(arr, columns=["a", "b", "c"]))

# ── 3. Inspecting a DataFrame ────────────────
print(df.head(3))        # first 3 rows
print(df.tail(2))        # last 2 rows
print(df.info())         # dtypes + null counts
print(df.describe())     # stats for numeric columns
print(df.sample(3))      # 3 random rows

# ── 4. Selecting data ────────────────────────

# Single column → Series
print(df["name"])

# Multiple columns → DataFrame
print(df[["name", "salary"]])

# Row selection with .loc (label-based) and .iloc (position-based)
print(df.loc[2])                        # row with index label 2
print(df.loc[1:3, "name":"city"])       # label slice (inclusive)
print(df.iloc[0])                       # first row by position
print(df.iloc[1:4, 0:3])               # position slice

# Boolean filtering
high_earners = df[df["salary"] > 60000]
print(high_earners)

nairobi_active = df[(df["city"] == "Nairobi") & (df["active"] == True)]
print(nairobi_active)

# ── 5. Adding & modifying columns ────────────
df["salary_usd"] = df["salary"] / 130      # KES → USD estimate
df["seniority"]  = df["age"].apply(lambda a: "senior" if a >= 30 else "junior")
print(df[["name", "seniority", "salary_usd"]].round(2))

# ── 6. Index management ──────────────────────
df2 = df.set_index("name")   # use name as row label
print(df2.loc["Alice"])

df3 = df2.reset_index()      # move index back to column
print(df3.columns.tolist())

# ── 7. Sorting ───────────────────────────────
print(df.sort_values("salary", ascending=False))
print(df.sort_values(["city", "age"]))   # multi-column sort

# ── 8. Basic stats ───────────────────────────
print(df["salary"].mean())      # average salary
print(df["salary"].median())
print(df["age"].value_counts()) # frequency of each age
print(df["city"].nunique())     # number of unique cities
print(df["active"].sum())       # number of True rows

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   Series          — 1D labelled array
#   DataFrame       — 2D labelled table
#   .loc / .iloc    — label-based vs position-based access
#   Boolean indexing — df[df["col"] > value]
#   .apply()        — apply a function to every row/cell
#   .describe()     — summary statistics
# ─────────────────────────────────────────────
