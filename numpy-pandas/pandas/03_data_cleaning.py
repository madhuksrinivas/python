# ─────────────────────────────────────────────
# PANDAS 03 — Data Cleaning
# ─────────────────────────────────────────────
#
# WHAT IS DATA CLEANING?
#   Real-world data is dirty — missing values, wrong types,
#   duplicates, inconsistent strings, outliers. Data scientists
#   spend 60-80% of their time here. Clean data directly
#   determines model quality: "garbage in, garbage out."
# ─────────────────────────────────────────────

import pandas as pd
import numpy as np

# Build a deliberately messy dataset
raw = pd.DataFrame({
    "id":        [1, 2, 3, 2, 4, 5, 6],
    "name":      ["Alice", "Bob", "carol ", "Bob", None, "EVE", "Frank"],
    "age":       [25, 30, None, 30, 200, 22, -5],
    "salary":    [55000, 72000, 88000, 72000, None, 49000, 61000],
    "city":      ["Nairobi", "London", "paris", "London", "Berlin", "NAIROBI", "Lagos"],
    "joined":    ["2022-03-01", "2020-07-15", "bad-date", "2020-07-15",
                  "2023-01-10", "2021-06-30", "2019-12-05"],
    "score":     [88, None, 91, None, 55, 77, 103],
})

print("=== Raw data ===")
print(raw)
print("\nNull counts:\n", raw.isnull().sum())

# ── 1. Handling missing values ────────────────

# Detect
print(raw.isnull())
print(raw.isnull().any(axis=1))     # rows with at least one null

# Drop rows where ALL values are null
df = raw.dropna(how="all")

# Drop rows with nulls in specific columns
df_strict = df.dropna(subset=["name", "salary"])
print("After drop:", df_strict.shape)

# Fill with a fixed value
df["score"] = df["score"].fillna(0)

# Fill with statistical measures (common in ML)
df["salary"] = df["salary"].fillna(df["salary"].median())
df["age"]    = df["age"].fillna(df["age"].mean())

# Forward-fill / backward-fill (time-series)
ts = pd.Series([1.0, None, None, 4.0, None, 6.0])
print(ts.ffill())    # 1 1 1 4 4 6  — fill with previous value
print(ts.bfill())    # 1 4 4 4 6 6  — fill with next value

# Interpolate (better for time-series)
print(ts.interpolate())   # 1.0 2.0 3.0 4.0 5.0 6.0

# ── 2. Removing duplicates ────────────────────
print("\nDuplicates:", df.duplicated().sum())          # 1
df = df.drop_duplicates()                             # drop exact duplicates
df = df.drop_duplicates(subset=["id"], keep="first")  # unique on id
print("After dedup:", df.shape)

# ── 3. Fixing data types ──────────────────────
# Parse dates — coerce=True turns unparseable values to NaT
df["joined"] = pd.to_datetime(df["joined"], errors="coerce")
print(df["joined"].dtype)   # datetime64[ns]
print(df["joined"].isna().sum())   # 1 (the "bad-date" row)

# Drop rows with bad dates
df = df.dropna(subset=["joined"])

# Cast columns
df["id"]     = df["id"].astype("int32")
df["salary"] = df["salary"].astype("float32")

# Use categorical dtype — saves memory for low-cardinality strings
df["city"] = df["city"].str.lower().str.strip().astype("category")
print(df["city"].dtype)   # category
print(df.memory_usage(deep=True))

# ── 4. String cleaning ────────────────────────
df["name"] = df["name"].str.strip()          # remove whitespace
df["name"] = df["name"].str.title()          # Title Case
df["city"] = df["city"].str.lower().str.strip()

# Replace values
df["city"] = df["city"].replace({"nairobi": "Nairobi",
                                  "paris":   "Paris",
                                  "london":  "London"})

# Extract with regex (e.g. get year from a string)
sample = pd.Series(["REF-2024-001", "REF-2025-042", "REF-2026-100"])
df_sample = sample.str.extract(r"REF-(\d{4})-(\d+)", expand=True)
df_sample.columns = ["year", "seq"]
print(df_sample)

# ── 5. Handling outliers ─────────────────────
# Strategy 1: IQR method
Q1  = df["salary"].quantile(0.25)
Q3  = df["salary"].quantile(0.75)
IQR = Q3 - Q1
df_no_outliers = df[(df["salary"] >= Q1 - 1.5 * IQR) &
                    (df["salary"] <= Q3 + 1.5 * IQR)]

# Strategy 2: Clip (cap) to a valid range
df["age"]   = df["age"].clip(lower=0, upper=120)
df["score"] = df["score"].clip(lower=0, upper=100)
print(df[["name", "age", "score"]])

# ── 6. Renaming & reordering columns ─────────
df = df.rename(columns={"id": "employee_id", "joined": "start_date"})
desired_order = ["employee_id", "name", "age", "city", "salary", "score", "start_date"]
df = df[[c for c in desired_order if c in df.columns]]
print(df.columns.tolist())

# ── 7. Summary after cleaning ────────────────
print("\n=== Clean data ===")
print(df)
print("\nDtypes:\n", df.dtypes)
print("\nNull counts:\n", df.isnull().sum())
print("\nDescribe:\n", df.describe())

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   isnull / fillna / dropna  — missing value handling
#   drop_duplicates           — remove duplicate rows
#   pd.to_datetime(errors="coerce")  — safe date parsing
#   str.strip / str.title / replace  — string normalisation
#   clip(lower, upper)        — cap outliers
#   astype("category")        — memory-efficient strings
#   IQR method                — statistical outlier removal
# ─────────────────────────────────────────────
