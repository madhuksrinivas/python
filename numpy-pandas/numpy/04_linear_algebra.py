# ─────────────────────────────────────────────
# NUMPY 04 — Linear Algebra (the heart of AI)
# ─────────────────────────────────────────────
#
# WHAT IS LINEAR ALGEBRA IN AI?
#   Every neural network layer is a matrix multiplication.
#   Every gradient update is a vector operation. Embeddings,
#   attention scores, PCA, SVD — all linear algebra.
#   NumPy's np.linalg module and the @ operator give you
#   optimised BLAS/LAPACK routines for all of these.
# ─────────────────────────────────────────────

import numpy as np

# ── 1. Dot product & matrix multiplication ───

# 1D dot product (inner product)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.dot(a, b))         # 32  (1*4 + 2*5 + 3*6)
print(a @ b)                # 32  — @ operator (Python 3.5+, preferred)

# Matrix × vector
W = np.array([[1, 2],
              [3, 4],
              [5, 6]])       # shape (3, 2)  — weight matrix
x = np.array([1, 2])        # shape (2,)    — input vector

print(W @ x)                # [5 11 17]  — (3,2) @ (2,) = (3,)

# Matrix × Matrix  — the core of a fully-connected layer
A = np.random.rand(4, 3)    # 4 samples, 3 features
W2 = np.random.rand(3, 5)   # 3 input features → 5 output neurons
out = A @ W2                # (4, 3) @ (3, 5) = (4, 5)
print(out.shape)            # (4, 5) — 4 samples, 5 activations

# ── 2. Transpose ─────────────────────────────
M = np.array([[1, 2, 3],
              [4, 5, 6]])   # (2, 3)

print(M.T)                  # (3, 2) — transpose
print(M.T.shape)            # (3, 2)

# W^T @ W  — Gram matrix (used in style transfer, kernel methods)
gram = M @ M.T
print(gram)

# ── 3. Determinant & inverse ─────────────────
A = np.array([[2., 1.],
              [5., 3.]])

print(np.linalg.det(A))     # 1.0
A_inv = np.linalg.inv(A)
print(A_inv)

# Verify: A @ A_inv ≈ identity
print(np.allclose(A @ A_inv, np.eye(2)))   # True

# ── 4. Solving linear systems  Ax = b ────────
# Example: 2x + y = 5, 5x + 3y = 14
A = np.array([[2., 1.],
              [5., 3.]])
b = np.array([5., 14.])
x = np.linalg.solve(A, b)    # preferred over inv(A) @ b
print(x)                     # [1. 3.]  — x=1, y=3

# ── 5. Eigenvalues & eigenvectors ────────────
# Used in PCA, spectral clustering, PageRank
cov = np.array([[4., 2.],
                [2., 3.]])
eigenvalues, eigenvectors = np.linalg.eig(cov)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# ── 6. Singular Value Decomposition (SVD) ────
# Used in: PCA, recommendation systems, image compression, NLP (LSA)
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9],
                 [1, 0, 2]], dtype=np.float64)

U, S, Vt = np.linalg.svd(data, full_matrices=False)
print("U shape:", U.shape)   # (4, 3)
print("S:", S)               # singular values (descending)
print("Vt shape:", Vt.shape) # (3, 3)

# Reconstruct (verify correctness)
reconstructed = U @ np.diag(S) @ Vt
print(np.allclose(data, reconstructed))  # True

# Low-rank approximation using top-k singular values (compression)
k = 1
low_rank = U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]
print("Low-rank approx:\n", low_rank.round(2))

# ── 7. Norms — distance & regularisation ─────
v = np.array([3.0, 4.0])
print(np.linalg.norm(v))          # 5.0    — L2 (Euclidean) norm
print(np.linalg.norm(v, ord=1))   # 7.0    — L1 (Manhattan) norm
print(np.linalg.norm(v, ord=np.inf))  # 4.0  — L∞ (max) norm

# Normalise a vector to unit length
unit = v / np.linalg.norm(v)
print(unit)                       # [0.6 0.8]
print(np.linalg.norm(unit))       # 1.0

# Batch cosine similarity — similarity between embeddings
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

emb1 = np.array([0.2, 0.9, 0.3])
emb2 = np.array([0.1, 0.8, 0.4])
print(cosine_similarity(emb1, emb2).round(4))    # ~0.99

# ── 8. Batch matrix multiply with np.einsum ──
# einsum is the most expressive contraction notation
# Format: 'output_subscripts,input_subscripts->output'

# Matrix multiply: i,j × j,k → i,k
A = np.random.rand(3, 4)
B = np.random.rand(4, 5)
print(np.einsum('ij,jk->ik', A, B).shape)   # (3, 5)

# Batched dot products: batch of vectors → batch of scalars
queries = np.random.rand(8, 64)   # 8 query vectors, dim 64
keys    = np.random.rand(8, 64)   # 8 key vectors
scores  = np.einsum('id,id->i', queries, keys)   # element-wise then sum
print(scores.shape)               # (8,)  — attention score per pair

# ─────────────────────────────────────────────
# WHAT YOU LEARNED
#   @          — matrix multiplication operator
#   .T         — transpose
#   linalg.solve   — Ax = b (stable, no inverse needed)
#   linalg.eig     — eigendecomposition (PCA base)
#   linalg.svd     — SVD for compression/recommendations
#   linalg.norm    — L1, L2, L∞ norms
#   einsum         — expressive tensor contraction
# ─────────────────────────────────────────────
