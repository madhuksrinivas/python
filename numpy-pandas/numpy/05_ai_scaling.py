# ─────────────────────────────────────────────
# NUMPY 05 — AI & Data Science Scaling Patterns
# ─────────────────────────────────────────────
#
# WHAT IS THIS FILE ABOUT?
#   When moving from toy datasets to production AI, NumPy
#   usage patterns matter enormously. This file covers the
#   real-world patterns used to preprocess training data,
#   implement forward passes, handle batching, and manage
#   memory — the same patterns used inside PyTorch/TensorFlow
#   before GPU dispatch.
# ─────────────────────────────────────────────

import numpy as np
import time

# ── 1. Generating synthetic datasets ─────────
np.random.seed(42)

# Classification dataset (N samples, D features, C classes)
N, D, C = 10_000, 128, 10
X = np.random.randn(N, D).astype(np.float32)   # feature matrix
y = np.random.randint(0, C, size=N)             # integer labels

print(f"X: {X.shape}, dtype={X.dtype}")   # (10000, 128) float32
print(f"y: {y.shape}, unique={np.unique(y)}")

# Regression dataset with noise
X_reg = np.linspace(0, 10, 500).reshape(-1, 1)
y_reg = 3.5 * X_reg.squeeze() + np.random.randn(500) * 2.0

# ── 2. Train / validation / test split ───────
def train_val_test_split(X, y, val=0.15, test=0.15, seed=42):
    rng = np.random.default_rng(seed)
    idx = rng.permutation(len(X))
    n_test = int(len(X) * test)
    n_val  = int(len(X) * val)
    return (X[idx[n_test + n_val:]], y[idx[n_test + n_val:]],
            X[idx[n_test:n_test + n_val]], y[idx[n_test:n_test + n_val]],
            X[idx[:n_test]],  y[idx[:n_test]])

X_tr, y_tr, X_val, y_val, X_te, y_te = train_val_test_split(X, y)
print(f"Train {X_tr.shape}, Val {X_val.shape}, Test {X_te.shape}")

# ── 3. Feature scaling (fit on train, apply everywhere) ──
class StandardScaler:
    def fit(self, X):
        self.mean_ = X.mean(axis=0)    # per-feature mean
        self.std_  = X.std(axis=0) + 1e-8   # avoid /0
        return self

    def transform(self, X):
        return (X - self.mean_) / self.std_

    def fit_transform(self, X):
        return self.fit(X).transform(X)

scaler = StandardScaler()
X_tr_scaled  = scaler.fit_transform(X_tr)
X_val_scaled = scaler.transform(X_val)    # use TRAIN stats only
X_te_scaled  = scaler.transform(X_te)

print(f"Scaled mean  ≈ 0: {X_tr_scaled.mean():.5f}")
print(f"Scaled std   ≈ 1: {X_tr_scaled.std():.5f}")

# ── 4. Mini-batch generator ───────────────────
def batch_iter(X, y, batch_size=64, shuffle=True, seed=None):
    """Yield (X_batch, y_batch) tuples indefinitely."""
    rng = np.random.default_rng(seed)
    n   = len(X)
    while True:
        idx = rng.permutation(n) if shuffle else np.arange(n)
        for start in range(0, n, batch_size):
            batch = idx[start:start + batch_size]
            yield X[batch], y[batch]

batches = batch_iter(X_tr_scaled, y_tr, batch_size=32)
Xb, yb = next(batches)
print(f"Batch shape: X={Xb.shape}, y={yb.shape}")   # (32, 128), (32,)

# ── 5. Manual neural-network forward pass ────
# Demonstrates what frameworks do under the hood.

def relu(z):
    return np.maximum(0, z)     # vectorised ReLU

def softmax(z):
    e = np.exp(z - z.max(axis=1, keepdims=True))   # stable softmax
    return e / e.sum(axis=1, keepdims=True)

def cross_entropy_loss(probs, labels):
    n = len(labels)
    return -np.log(probs[np.arange(n), labels] + 1e-9).mean()

# Random weight initialisation (He init — good for ReLU)
np.random.seed(0)
W1 = np.random.randn(D, 64).astype(np.float32) * np.sqrt(2.0 / D)
b1 = np.zeros(64, dtype=np.float32)
W2 = np.random.randn(64, C).astype(np.float32) * np.sqrt(2.0 / 64)
b2 = np.zeros(C, dtype=np.float32)

# Forward pass on a single batch
Z1 = Xb @ W1 + b1              # (32, 64)
A1 = relu(Z1)                   # (32, 64)
Z2 = A1 @ W2 + b2              # (32, C)
probs = softmax(Z2)             # (32, C)  — probabilities
loss  = cross_entropy_loss(probs, yb)
preds = probs.argmax(axis=1)
acc   = (preds == yb).mean()
print(f"Loss: {loss:.4f}  Acc: {acc:.2%}")

# ── 6. Memory layout — C vs Fortran order ────
# C-contiguous (row-major) is faster for row-wise access.
# Fortran-contiguous (column-major) is faster for column-wise.
C_arr = np.ascontiguousarray(X)    # ensure C order (default)
F_arr = np.asfortranarray(X)

print(C_arr.flags['C_CONTIGUOUS'])   # True
print(F_arr.flags['F_CONTIGUOUS'])   # True

# ── 7. Saving and loading arrays ─────────────
# Binary .npy — fast, preserves dtype/shape exactly
np.save('/tmp/features.npy', X_tr_scaled)
loaded = np.load('/tmp/features.npy')
print(np.allclose(X_tr_scaled, loaded))   # True

# .npz — compressed archive of multiple arrays
np.savez_compressed('/tmp/dataset.npz',
                    X_train=X_tr_scaled, y_train=y_tr,
                    X_val=X_val_scaled,  y_val=y_val)
ds = np.load('/tmp/dataset.npz')
print(list(ds.keys()))   # ['X_train', 'y_train', 'X_val', 'y_val']

# ── 8. Profiling memory usage ─────────────────
def array_memory(arr):
    mb = arr.nbytes / 1024 / 1024
    print(f"  {arr.dtype} {arr.shape} → {mb:.2f} MB")

print("Memory footprint:")
array_memory(np.ones((1000, 1000), dtype=np.float64))   # 7.63 MB
array_memory(np.ones((1000, 1000), dtype=np.float32))   # 3.81 MB
array_memory(np.ones((1000, 1000), dtype=np.float16))   # 1.91 MB
# float16 (half-precision) is used in mixed-precision training on GPUs

# ── 9. Random number generation (modern API) ─
rng = np.random.default_rng(seed=2026)

dropout_mask = rng.random((32, 64)) > 0.5   # 50% dropout mask
print(dropout_mask.mean().round(2))          # ~0.5

noise = rng.normal(loc=0, scale=0.01, size=(32, 64)).astype(np.float32)
augmented = Xb + noise[:, :D]               # add Gaussian noise for augmentation

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   float32 vs float64  — memory & GPU compatibility
#   StandardScaler      — fit on train, transform all splits
#   Mini-batch iteration — random permutation every epoch
#   Forward pass        — matmul + ReLU + softmax + cross-entropy
#   np.save / np.savez_compressed — binary array persistence
#   default_rng         — reproducible modern random API
#   float16             — half-precision for GPU memory savings
# ─────────────────────────────────────────────
