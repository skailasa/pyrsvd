import numpy as np
import pytest

import pyrsvd


np.random.seed(0)

@pytest.fixture
def A():
    return np.random.rand(123, 45)


@pytest.fixture
def K():
    return 100


def test_svd(A, K):

    cu, cs, cvt = np.linalg.svd(A, full_matrices=False)

    du, ds, dvt = pyrsvd.svd(A, K)

    rec_cpu = cu @ np.diag(cs) @ cvt
    rec_gpu = du @ np.diag(ds) @ dvt

    assert np.allclose(rec_gpu, rec_cpu)
