# NumPy vs Pandas

---

## 1. What is NumPy?

**NumPy** (Numerical Python) is a foundational Python library for **numerical computing**. It provides:

- A powerful **N-dimensional array** object (`ndarray`)
- Mathematical functions to operate on arrays (linear algebra, Fourier transforms, random number generation)
- Tools for integrating C/C++ and Fortran code

NumPy arrays are **homogeneous** — all elements must be the same data type (e.g., all `int64` or all `float32`). This makes operations extremely fast because data is stored in contiguous memory blocks.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr * 2)        # [2 4 6 8 10]
print(arr.mean())     # 3.0

matrix = np.zeros((3, 3))   # 3x3 matrix of zeros
```

**Primary use:** Mathematical and scientific computing, machine learning (under the hood), image processing, simulations.

---

## 2. What is Pandas?

**Pandas** is a Python library built **on top of NumPy** for **data manipulation and analysis**. It provides:

- **Series** — a 1D labeled array (like a column in a spreadsheet)
- **DataFrame** — a 2D labeled table (like a full spreadsheet / SQL table)
- Tools for reading/writing CSV, Excel, JSON, SQL databases
- Powerful data cleaning, filtering, grouping, and aggregation

Pandas columns can hold **different data types** (strings, integers, dates, booleans) in the same table, making it ideal for real-world datasets.

```python
import pandas as pd

df = pd.read_csv("data.csv")
print(df.head())
print(df["age"].mean())
print(df[df["salary"] > 50000])   # filter rows
print(df.groupby("department")["salary"].sum())
```

**Primary use:** Data wrangling, exploratory data analysis (EDA), working with tabular/structured data, data pipelines.

---

## 3. NumPy vs Pandas — Key Differences

| Feature                    | NumPy                                           | Pandas                                       |
| -------------------------- | ----------------------------------------------- | -------------------------------------------- |
| **Core data structure**    | `ndarray` (N-dimensional array)                 | `Series` (1D) and `DataFrame` (2D)           |
| **Data types**             | Homogeneous (all same type per array)           | Heterogeneous (each column can differ)       |
| **Indexing**               | Integer-based (positional)                      | Label-based (row/column names)               |
| **Primary purpose**        | Numerical / mathematical computation            | Data manipulation and analysis               |
| **Missing values**         | No native support (`nan` is a float workaround) | Built-in support (`NaN`, `NaT`, `pd.NA`)     |
| **Column labels**          | No column names                                 | Named columns and row labels                 |
| **Reading files**          | No built-in file I/O                            | Read CSV, Excel, JSON, SQL, Parquet, etc.    |
| **Grouping / aggregation** | Manual loops or advanced indexing               | Built-in `groupby()`, `pivot_table()`        |
| **String operations**      | No string methods on arrays                     | `Series.str.upper()`, `str.contains()`, etc. |
| **Performance**            | Faster for pure math on uniform data            | Slightly slower but far more feature-rich    |
| **Memory layout**          | Contiguous block (cache-friendly)               | More overhead due to labels and mixed types  |
| **Dimensions**             | Supports N dimensions (1D, 2D, 3D...)           | Primarily 2D (DataFrame)                     |
| **Built on**               | C under the hood                                | Built on top of NumPy                        |

---

## 4. When to Use What?

### Use NumPy when:

- You need fast **matrix / vector math** (dot products, eigenvalues, FFT)
- Working with **images** (pixel arrays), **audio**, or **raw numerical data**
- Building or using **machine learning algorithms** from scratch
- Data is uniformly typed and operations are element-wise
- You need **multi-dimensional arrays** (3D, 4D tensors)

```python
# Matrix multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B))
```

### Use Pandas when:

- Working with **CSV, Excel, database** data
- Data has **mixed types** (names, ages, dates, salaries)
- You need to **filter, sort, group, merge** datasets
- Doing **exploratory data analysis (EDA)**
- Cleaning messy real-world data (missing values, duplicates)

```python
# Group and aggregate
df.groupby("country")["revenue"].sum().sort_values(ascending=False)
```

---

## 5. Quick Summary

```
NumPy  →  raw number crunching, math, arrays, ML internals
Pandas →  tables, CSV files, data cleaning, analysis, EDA
```

They work **together** — Pandas uses NumPy arrays internally, and you can convert between them:

```python
df["price"].to_numpy()          # Pandas Series → NumPy array
pd.Series(np.array([1, 2, 3]))  # NumPy array  → Pandas Series
```
