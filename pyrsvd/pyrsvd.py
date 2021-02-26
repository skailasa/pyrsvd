"""
Randomised Singular Value Decompositions
"""

import cupy as cp


def svd(A, K, full_matrices=False):
    """
    Compute randomised SVD of a dense matrix A on CUDA device.

    Parameters:
    -----------
    A : np.array(shape=(M, N), dtype=np.float32)
        Compute the Randomised SVD of a 'thin' and 'tall' matrix, i.e. M > N
    K : np.int32
        Target compression rank.

    Returns:
    --------
    (np.array(dtype=np.float32))
        Return CPU arrays of (u, s, vt) respectively.
    """

    width = len(A[0])

    dA = cp.asarray(A)

    dOmega = cp.random.rand(width, K)
    dY = dA @ dOmega

    dQ, _ = cp.linalg.qr(dY)

    dB = dQ.T @ dA

    du, dS, dVT = cp.linalg.svd(dB, full_matrices=full_matrices)
    dU = dQ @ du

    return dU.get(), dS.get(), dVT.get()
