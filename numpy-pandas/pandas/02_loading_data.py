# ─────────────────────────────────────────────
# PANDAS 02 — Loading Data & Exporting
# ─────────────────────────────────────────────
#
# WHAT IS THIS FILE ABOUT?
#   Real data lives in CSV files, Excel sheets, JSON APIs,
#   and SQL databases. Pandas can read all of them with a
#   single function call. You'll also learn how to write
#   data back out, which is essential for saving cleaned
#   datasets or model predictions.
# ─────────────────────────────────────────────

import pandas as pd
import numpy as np
import io
import os

# ── 1. Creating sample data files ─────────────
# (In real projects you'd use actual files; we build them here.)
CSV_PATH  = "/tmp/pd_sales.csv"
JSON_PATH = "/tmp/pd_products.json"
EXCEL_PATH = "/tmp/pd_report.xlsx"   # requires: pip install openpyxl

sample_csv = """date,product,region,units,revenue
2026-01-05,Widget A,East,120,2400.00
2026-01-06,Widget B,West,85,3400.00
2026-01-07,Widget A,West,200,4000.00
2026-01-08,Gadget X,East,50,7500.00
2026-01-09,Widget B,East,95,3800.00
2026-01-10,Gadget X,West,40,6000.00
2026-01-11,Widget A,East,,
2026-01-12,Widget B,West,110,4400.00
"""
with open(CSV_PATH, "w") as f:
    f.write(sample_csv)

# ── 2. Reading CSV ────────────────────────────
df = pd.read_csv(CSV_PATH)
print(df)
print(df.dtypes)

# Useful read_csv options
df = pd.read_csv(
    CSV_PATH,
    parse_dates=["date"],      # auto-parse date column
    dtype={"units": "Int64"},  # nullable integer
)
print(df.dtypes)
print(df["date"].dt.month)     # extract month from datetime

# Read from a URL (requires network)
# df = pd.read_csv("https://raw.githubusercontent.com/datasets/...")

# Read only specific columns (saves memory on huge files)
df_small = pd.read_csv(CSV_PATH, usecols=["date", "product", "revenue"])
print(df_small.head())

# Read in chunks (essential for files larger than RAM)
chunk_size = 3
for chunk in pd.read_csv(CSV_PATH, chunksize=chunk_size):
    print(f"Chunk: {chunk.shape}")
    # process each chunk independently

# ── 3. Reading JSON ───────────────────────────
import json
products = [
    {"id": 1, "name": "Widget A", "price": 20.0, "category": "hardware"},
    {"id": 2, "name": "Widget B", "price": 40.0, "category": "hardware"},
    {"id": 3, "name": "Gadget X", "price": 150.0, "category": "electronics"},
]
with open(JSON_PATH, "w") as f:
    json.dump(products, f)

df_json = pd.read_json(JSON_PATH)
print(df_json)

# Normalise nested JSON  (e.g. API responses)
nested = [
    {"order_id": 1, "customer": {"name": "Alice", "city": "Nairobi"}},
    {"order_id": 2, "customer": {"name": "Bob",   "city": "London"}},
]
flat = pd.json_normalize(nested, sep="_")
print(flat.columns.tolist())   # ['order_id', 'customer_name', 'customer_city']
print(flat)

# ── 4. Reading from an in-memory string ──────
csv_str = "a,b,c\n1,2,3\n4,5,6\n"
df_mem = pd.read_csv(io.StringIO(csv_str))
print(df_mem)

# ── 5. Reading SQL (sqlite3 example) ─────────
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE scores (name TEXT, score REAL)")
conn.executemany("INSERT INTO scores VALUES (?,?)",
                 [("Alice", 92), ("Bob", 87), ("Carol", 95)])
conn.commit()

df_sql = pd.read_sql("SELECT * FROM scores ORDER BY score DESC", conn)
print(df_sql)
conn.close()

# ── 6. Writing data ───────────────────────────
df = pd.read_csv(CSV_PATH, parse_dates=["date"])

# CSV
df.to_csv("/tmp/pd_output.csv", index=False)    # index=False avoids extra column

# JSON
df.dropna().to_json("/tmp/pd_output.json", orient="records", indent=2)

# Excel (needs openpyxl: pip install openpyxl)
try:
    df.dropna().to_excel(EXCEL_PATH, index=False, sheet_name="Sales")
    print("Excel written")
except ImportError:
    print("openpyxl not installed — skip Excel write")

# Parquet — columnar format, ideal for large ML datasets
# (needs pyarrow: pip install pyarrow)
try:
    df.dropna().to_parquet("/tmp/pd_output.parquet", index=False)
    df_pq = pd.read_parquet("/tmp/pd_output.parquet")
    print("Parquet round-trip OK:", df_pq.shape)
except ImportError:
    print("pyarrow not installed — skip Parquet write")

# ── 7. Inspecting what you loaded ────────────
df = pd.read_csv(CSV_PATH)
print("\n--- Quick inspection ---")
print("Shape:",      df.shape)
print("Columns:",    df.columns.tolist())
print("Null counts:\n", df.isnull().sum())
print("Memory usage:", df.memory_usage(deep=True).sum() // 1024, "KB")

# ── Cleanup ───────────────────────────────────
for p in [CSV_PATH, JSON_PATH, "/tmp/pd_output.csv", "/tmp/pd_output.json"]:
    if os.path.exists(p): os.remove(p)

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   read_csv(parse_dates, dtype, usecols, chunksize)
#   read_json / json_normalize  — flat nested data
#   read_sql                    — query databases directly
#   to_csv / to_json / to_excel / to_parquet
#   Parquet                     — best format for large ML data
#   Chunked reading             — handle files bigger than RAM
# ─────────────────────────────────────────────
