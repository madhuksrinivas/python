# ─────────────────────────────────────────────
# NUMPY 02 — Vectorised Operations & Broadcasting
# ─────────────────────────────────────────────
#
# WHAT IS VECTORISATION?
#   Instead of looping over elements in Python (slow), you
#   apply an operation to the entire array at once. NumPy
#   dispatches the operation to optimised C/BLAS routines
#   that can use SIMD CPU instructions. A loop that takes
#   seconds becomes microseconds. This is how deep learning
#   frameworks (PyTorch, TensorFlow) achieve their speed.
# ─────────────────────────────────────────────

import numpy as np
import time

# ── 1. Element-wise arithmetic ───────────────
a = np.array([1, 2, 3, 4, 5], dtype=np.float64)
b = np.array([10, 20, 30, 40, 50], dtype=np.float64)

print(a + b)        # [11. 22. 33. 44. 55.]
print(a * b)        # [10. 40. 90. 160. 250.]
print(b / a)        # [10. 10. 10. 10. 10.]
print(a ** 2)       # [ 1.  4.  9. 16. 25.]
print(np.sqrt(a))   # [1.  1.41 1.73 2.  2.24]

# ── 2. Speed: vectorised vs Python loop ──────
N = 10_000_000
x = np.random.rand(N).astype(np.float32)

start = time.perf_counter()
py_result = [v * 2 for v in x]
print(f"Python loop : {time.perf_counter() - start:.3f}s")

start = time.perf_counter()
np_result = x * 2
print(f"NumPy vector: {time.perf_counter() - start:.3f}s")
# NumPy is typically 50-200× faster here

# ── 3. Universal functions (ufuncs) ──────────
angles = np.linspace(0, np.pi, 6)
print(np.sin(angles).round(3))      # [0.  0.588 0.951 0.951 0.588 0.]
print(np.exp(np.array([0, 1, 2])))  # [1.  2.718 7.389]
print(np.log(np.array([1, np.e, np.e**2])))  # [0. 1. 2.]

# ── 4. Aggregations ──────────────────────────
data = np.array([[4, 7, 2, 1],
                 [9, 3, 8, 5],
                 [6, 0, 4, 3]])

print(data.sum())               # 52  (all elements)
print(data.sum(axis=0))         # [19 10 14  9]  — sum each column
print(data.sum(axis=1))         # [14 25 13]     — sum each row
print(data.min(), data.max())   # 0 9
print(data.mean())              # 4.333...
print(data.std())               # standard deviation
print(data.argmax())            # 4 — flat index of max element
print(np.unravel_index(data.argmax(), data.shape))  # (1, 0) — row, col

# Cumulative operations
print(np.cumsum(np.array([1, 2, 3, 4])))   # [1  3  6 10]
print(np.cumprod(np.array([1, 2, 3, 4])))  # [1  2  6 24]

# ── 5. Broadcasting — the killer feature ─────
# Broadcasting lets arrays of DIFFERENT SHAPES operate together
# by "stretching" the smaller array across the larger one.

# Scalar broadcast
arr = np.array([1, 2, 3, 4])
print(arr * 10)       # [10 20 30 40]  — scalar broadcast to all elements

# 1D + 2D broadcast (add a bias vector to every row of a matrix)
weights = np.array([[0.1, 0.2, 0.3],
                    [0.4, 0.5, 0.6]])   # shape (2, 3)
bias    = np.array([1.0, 2.0, 3.0])    # shape (3,)

print(weights + bias)   # bias broadcast across rows:
# [[1.1 2.2 3.3]
#  [1.4 2.5 3.6]]

# Column broadcast — reshape bias to (2,1) to add to each column
col_bias = np.array([[10.], [20.]])     # shape (2, 1)
print(weights + col_bias)
# [[10.1 10.2 10.3]
#  [20.4 20.5 20.6]]

# Broadcasting rules (shapes align right-to-right):
# (2,3) + (3,)  → OK,  (3,) stretches to (2,3)
# (2,1) + (1,3) → OK,  both stretch to (2,3)
# (2,3) + (2,4) → ERROR, mismatched non-1 dimensions

# ── 6. Comparison & boolean operations ───────
scores = np.array([88, 42, 95, 61, 73, 55, 90])
print(scores > 70)                    # [T F T F T F T]
print(scores[scores > 70])            # [88 95 73 90]  — boolean indexing
print(np.sum(scores > 70))            # 4  (count passing)
print(np.where(scores >= 70, "pass", "fail"))

# np.where as vectorised if/else (used everywhere in ML pipelines)
clipped = np.where(scores > 80, 80, scores)  # cap at 80
print(clipped)   # [80 42 80 61 73 55 80]

# ── 7. Normalisation — fundamental in ML ─────
raw = np.array([200, 150, 300, 50, 250], dtype=np.float32)

# Min-max normalisation → [0, 1]
norm_minmax = (raw - raw.min()) / (raw.max() - raw.min())
print(norm_minmax.round(3))

# Z-score (standardisation) → mean=0, std=1
norm_z = (raw - raw.mean()) / raw.std()
print(norm_z.round(3))

# Softmax — converts raw scores to probabilities (used in classifiers)
def softmax(x):
    e_x = np.exp(x - x.max())    # subtract max for numerical stability
    return e_x / e_x.sum()

logits = np.array([2.0, 1.0, 0.1])
print(softmax(logits).round(3))   # [0.659 0.242 0.099] — sums to 1

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   Vectorised ops      — no Python loops needed
#   ufuncs              — sin, exp, log applied element-wise
#   axis=0/1            — aggregate along rows or columns
#   Broadcasting        — operations on different-shaped arrays
#   Boolean indexing    — filter rows/cols with a mask
#   np.where            — vectorised if/else
#   Normalisation       — min-max, z-score, softmax
# ─────────────────────────────────────────────
