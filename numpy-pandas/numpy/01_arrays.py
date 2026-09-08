# ─────────────────────────────────────────────
# NUMPY 01 — Arrays & ndarray Basics
# ─────────────────────────────────────────────
#
# WHAT IS NUMPY?
#   NumPy (Numerical Python) is the foundation of the entire
#   Python data science and AI stack. It provides the ndarray
#   — a fast, memory-efficient multi-dimensional array stored
#   in a contiguous block of typed memory (like C/Fortran).
#   Operations run in compiled C code, making them 10-100×
#   faster than equivalent Python loops.
#   Install: pip install numpy
# ─────────────────────────────────────────────

import numpy as np

print("NumPy version:", np.__version__)

# ── 1. Creating arrays ───────────────────────

# From a Python list
a = np.array([1, 2, 3, 4, 5])
print(a)              # [1 2 3 4 5]
print(type(a))        # <class 'numpy.ndarray'>

# 2D array (matrix)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(matrix)
print(matrix.shape)   # (3, 3)  — rows, cols
print(matrix.ndim)    # 2       — number of dimensions
print(matrix.size)    # 9       — total elements
print(matrix.dtype)   # int64   — element data type

# ── 2. Array creation functions ──────────────
print(np.zeros((3, 4)))          # 3×4 matrix of 0.0
print(np.ones((2, 3)))           # 2×3 matrix of 1.0
print(np.full((2, 2), 7))        # 2×2 matrix filled with 7
print(np.eye(4))                 # 4×4 identity matrix
print(np.empty((2, 3)))          # uninitialized (fast allocation)

# Sequences
print(np.arange(0, 10, 2))       # [0 2 4 6 8]  like range()
print(np.linspace(0, 1, 5))      # [0. .25 .5 .75 1.]  — 5 evenly spaced

# ── 3. Data types — critical for AI performance ──
# Choosing the right dtype saves memory and speeds up GPU transfer.
f32 = np.array([1.0, 2.0, 3.0], dtype=np.float32)   # 4 bytes/elem (GPU default)
f64 = np.array([1.0, 2.0, 3.0], dtype=np.float64)   # 8 bytes/elem (CPU default)
i8  = np.array([1, 2, 3],       dtype=np.int8)       # 1 byte/elem

print(f32.dtype, f32.nbytes)    # float32 12
print(f64.dtype, f64.nbytes)    # float64 24 — twice the memory

# Cast dtype
x = np.array([1, 2, 3], dtype=np.int32)
y = x.astype(np.float32)
print(y.dtype)                  # float32

# ── 4. Reshaping ─────────────────────────────
flat = np.arange(12)            # [0 1 2 ... 11]
grid = flat.reshape(3, 4)       # 3 rows, 4 cols
print(grid)

cube = flat.reshape(2, 2, 3)    # 3D tensor (batch, rows, cols)
print(cube.shape)               # (2, 2, 3)

# -1 means "infer this dimension"
auto = flat.reshape(4, -1)      # 4 rows, NumPy computes cols=3
print(auto.shape)               # (4, 3)

# Flatten back to 1D
print(grid.flatten())           # always returns a copy
print(grid.ravel())             # returns a view when possible (faster)

# ── 5. Stacking & splitting ───────────────────
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.concatenate([a, b]))         # [1 2 3 4 5 6]
print(np.stack([a, b]))               # [[1 2 3] [4 5 6]]  — new axis
print(np.vstack([a, b]))              # same, vertical stack
print(np.hstack([a, b]))              # [1 2 3 4 5 6]

chunks = np.split(np.arange(9), 3)   # split into 3 equal arrays
print(chunks)

# ── 6. Copies vs views — IMPORTANT ───────────
original = np.array([1, 2, 3, 4, 5])
view     = original[1:4]             # slice is a VIEW, not a copy
view[0]  = 99
print(original)                      # [1 99 3 4 5] — original changed!

copy = original[1:4].copy()          # explicit copy breaks the link
copy[0] = 0
print(original)                      # unchanged

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   np.array()          — create ndarray from list
#   shape, ndim, size, dtype  — array metadata
#   zeros, ones, eye, arange, linspace  — constructors
#   dtype selection     — float32 for GPU, float64 for precision
#   reshape(-1, n)      — flexible dimension inference
#   view vs copy        — slices share memory; .copy() to isolate
# ─────────────────────────────────────────────
