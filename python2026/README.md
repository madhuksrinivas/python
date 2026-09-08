# Python 2026 — Complete Tutorial

A self-contained Python tutorial from zero to advanced.
Each file is a runnable `.py` script with explanations, sample code, and expected output in comments.

---

## basics/

| File                        | Topic                                                |
| --------------------------- | ---------------------------------------------------- |
| `01_hello_world.py`         | print(), comments, escape sequences                  |
| `02_variables_datatypes.py` | Variables, int/float/str/bool/None, casting          |
| `03_user_input.py`          | input(), f-strings, number formatting                |
| `04_operators.py`           | Arithmetic, comparison, logical, bitwise, membership |
| `05_strings.py`             | Indexing, slicing, methods, f-string format specs    |
| `06_conditionals.py`        | if/elif/else, ternary, match/case (3.10+)            |
| `07_loops.py`               | for, while, break, continue, enumerate, zip          |
| `08_lists.py`               | CRUD, sorting, slicing, unpacking                    |
| `09_tuples.py`              | Immutability, unpacking, namedtuple                  |
| `10_dictionaries.py`        | CRUD, iteration, comprehension, merge                |
| `11_sets.py`                | Set operations, frozenset, duplicate removal         |
| `12_functions.py`           | def, \*args/\*\*kwargs, scope, recursion             |
| `13_modules.py`             | import, from…import, **name**, packages              |
| `14_error_handling.py`      | try/except/else/finally, raise, custom exceptions    |

## advanced/

| File                      | Topic                                                 |
| ------------------------- | ----------------------------------------------------- |
| `01_comprehensions.py`    | List/dict/set comprehensions, generator expressions   |
| `02_lambda_map_filter.py` | lambda, map(), filter(), reduce()                     |
| `03_oop.py`               | Classes, inheritance, super(), @property, dataclasses |
| `04_file_io.py`           | Text files, JSON, CSV, pathlib                        |
| `05_decorators.py`        | Writing decorators, @functools.wraps, @cache          |
| `06_generators.py`        | yield, yield from, send(), itertools                  |
| `07_context_managers.py`  | **enter**/**exit**, @contextmanager, ExitStack        |
| `08_regex.py`             | re module, groups, flags, lookahead/lookbehind        |
| `09_type_hints.py`        | Annotations, Optional, Union, TypeVar, Protocol       |
| `10_concurrency.py`       | threading, multiprocessing, asyncio, async/await      |

## numpy/

> **What is NumPy?** The foundation of all Python data science and AI. Provides the `ndarray` — a fast, typed, multi-dimensional array backed by C. Operations run 10–100× faster than Python loops.

| File                   | Topic                                                                                                        |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| `01_arrays.py`         | ndarray creation, shape/dtype/size, reshape, views vs copies                                                 |
| `02_operations.py`     | Vectorisation, ufuncs, aggregation, broadcasting, normalisation, softmax                                     |
| `03_indexing.py`       | Boolean masking, fancy indexing, one-hot encoding, sliding windows                                           |
| `04_linear_algebra.py` | `@` operator, SVD, eigenvalues, cosine similarity, `einsum`                                                  |
| `05_ai_scaling.py`     | Train/val/test split, StandardScaler, mini-batch generator, manual forward pass, float16, `.npz` persistence |

```bash
pip install numpy
python numpy/01_arrays.py
```

---

## pandas/

> **What is Pandas?** Python's most important data manipulation library. Provides `Series` (1D) and `DataFrame` (2D table) for loading, cleaning, analysing, and exporting data — the backbone of every ML pipeline before model training.

| File                        | Topic                                                                                   |
| --------------------------- | --------------------------------------------------------------------------------------- |
| `01_series_dataframe.py`    | Series, DataFrame creation, `.loc`/`.iloc`, boolean filtering                           |
| `02_loading_data.py`        | CSV, JSON, SQL, chunked reading, Parquet export                                         |
| `03_data_cleaning.py`       | Nulls, duplicates, type casting, outliers, string normalisation                         |
| `04_analysis.py`            | `groupby`, pivot tables, joins, time-series resampling, correlation                     |
| `05_feature_engineering.py` | Log transforms, binning, one-hot/target encoding, memory optimisation, handoff to NumPy |

```bash
pip install pandas pyarrow openpyxl scikit-learn
python pandas/01_series_dataframe.py
```

---

## Learning path

```
basics/ (01 → 14)  →  advanced/ (01 → 10)  →  numpy/ (01 → 05)  →  pandas/ (01 → 05)
```

## How to run any file

```bash
python basics/01_hello_world.py
python advanced/03_oop.py
python numpy/04_linear_algebra.py
python pandas/05_feature_engineering.py
```

**Python version requirements**

- 3.10+ — `match/case` (basics/06)
- 3.11+ — `asyncio.TaskGroup` (advanced/10)
- 3.9+ — `list[str]` type hint syntax (advanced/09)

**Install all dependencies at once**

```bash
pip install numpy pandas pyarrow openpyxl scikit-learn
```
