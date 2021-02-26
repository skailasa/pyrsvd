"""
Randomised Singular Value Decompositions
"""

import cupy as cp


BLOCK_HEIGHT = 1024
BLOCK_WIDTH = 32

TPB = 32


def svd(A, K, full_matrices=False):
    """
    Compute SVD of a dense matrix A.
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
