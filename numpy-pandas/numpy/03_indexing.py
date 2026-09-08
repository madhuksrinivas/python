# ─────────────────────────────────────────────
# NUMPY 03 — Indexing, Slicing & Fancy Indexing
# ─────────────────────────────────────────────
#
# WHAT IS FANCY INDEXING?
#   Beyond basic slicing, NumPy lets you index with arrays of
#   integers or boolean masks. This is how you select specific
#   samples from a dataset, apply a mask to remove outliers,
#   or gather predictions for particular class labels — all
#   without a single Python loop.
# ─────────────────────────────────────────────

import numpy as np

# ── 1. Basic 1D indexing ─────────────────────
a = np.array([10, 20, 30, 40, 50, 60, 70, 80])

print(a[2])         # 30
print(a[-1])        # 80
print(a[2:6])       # [30 40 50 60]
print(a[::2])       # [10 30 50 70]   — every 2nd
print(a[::-1])      # [80 70 ... 10]  — reversed

# ── 2. 2D indexing ───────────────────────────
M = np.array([[1,  2,  3,  4],
              [5,  6,  7,  8],
              [9, 10, 11, 12]])

print(M[1, 2])          # 7          — row 1, col 2
print(M[0])             # [1 2 3 4]  — entire row 0
print(M[:, 2])          # [3 7 11]   — entire col 2
print(M[1:, 1:3])       # submatrix rows 1-2, cols 1-2

# Selecting specific rows
print(M[[0, 2]])        # rows 0 and 2: [[1 2 3 4],[9 10 11 12]]

# ── 3. Boolean (mask) indexing ───────────────
data = np.array([14, -3, 8, -7, 22, 0, -1, 5])

mask = data > 0
print(mask)                   # [T F T F T F F T]
print(data[mask])             # [14  8 22  5]

# Inline: remove outliers beyond 2 standard deviations
samples = np.random.normal(loc=100, scale=15, size=1000)
clean   = samples[np.abs(samples - samples.mean()) < 2 * samples.std()]
print(f"Original: {len(samples)}, After outlier removal: {len(clean)}")

# Modify in place using a mask
arr = np.array([1.0, -2.0, 3.0, -4.0, 5.0])
arr[arr < 0] = 0      # ReLU activation
print(arr)            # [1. 0. 3. 0. 5.]

# ── 4. Fancy indexing with integer arrays ────
prices = np.array([9.99, 14.99, 4.50, 29.99, 7.00, 19.99])
picks  = np.array([2, 0, 4])          # select items 2, 0, 4
print(prices[picks])                  # [4.5 9.99 7.0]

# 2D fancy: select specific (row, col) pairs
X = np.arange(16).reshape(4, 4)
rows = np.array([0, 1, 3])
cols = np.array([2, 1, 3])
print(X[rows, cols])    # [2 5 15]  — (0,2), (1,1), (3,3)

# ── 5. np.ix_ — outer-product style selection ─
# Select a submatrix using two index arrays (rows × cols)
row_idx = np.array([0, 2])
col_idx = np.array([1, 3])
print(X[np.ix_(row_idx, col_idx)])
# [[1  3]
#  [9 11]]

# ── 6. Structured indexing patterns in ML ────

# One-hot encoding rows for a batch of class labels
def one_hot(labels, n_classes):
    """Convert integer labels to one-hot matrix."""
    batch = labels.shape[0]
    oh    = np.zeros((batch, n_classes), dtype=np.float32)
    oh[np.arange(batch), labels] = 1.0
    return oh

labels = np.array([0, 2, 1, 3, 2])
print(one_hot(labels, n_classes=4))
# [[1 0 0 0]
#  [0 0 1 0]
#  [0 1 0 0]
#  [0 0 0 1]
#  [0 0 1 0]]

# Gather logits for the correct class (cross-entropy loss step)
logits = np.array([[2.0, 0.5, 0.3],
                   [0.1, 2.8, 0.9],
                   [1.2, 0.4, 3.1]])
true_labels = np.array([0, 1, 2])
correct_logits = logits[np.arange(len(true_labels)), true_labels]
print(correct_logits)   # [2.0 2.8 3.1]  — score for correct class per sample

# ── 7. np.take & np.put ──────────────────────
arr = np.array([100, 200, 300, 400, 500])
print(np.take(arr, [1, 3, 4]))          # [200 400 500]

out = np.zeros(5, dtype=int)
np.put(out, [1, 3], [99, 77])
print(out)                               # [  0  99   0  77   0]

# ── 8. Advanced slicing: stride tricks ───────
# Create rolling windows without copying data (used in time-series ML)
from numpy.lib.stride_tricks import sliding_window_view

signal = np.arange(10, dtype=np.float32)
windows = sliding_window_view(signal, window_shape=3)
print(windows)
# [[0. 1. 2.]
#  [1. 2. 3.]
#  ...
#  [7. 8. 9.]]

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   arr[mask]           — boolean indexing
#   arr[arr < 0] = 0    — in-place masking (ReLU pattern)
#   fancy indexing      — arr[[0, 2, 4]]
#   np.ix_             — cross-product row/col selection
#   one-hot encoding    — arr[range(n), labels] = 1
#   sliding_window_view — zero-copy rolling windows
# ─────────────────────────────────────────────
