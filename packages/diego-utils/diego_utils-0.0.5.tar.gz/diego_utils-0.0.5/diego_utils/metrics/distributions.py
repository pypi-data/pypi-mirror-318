"""Module to analyse and compare distributions.

The functionality is divided into two main types:
 - Distribution Comparison: Functionality to compare two distributions.
 - Distribution Analysis: Functionality to analyse a distribution.
"""

from typing import List, Tuple

import numpy as np
from scipy import stats


def ks_test_with_normal(data: List[int]) -> Tuple[float, float]:
    """
    Perform a Kolmogorov-Smirnov test comparing the given data to a normal distribution.

    Args:
        data (List[int]): The data to compare.

    Returns
    -------
        Tuple[float, float]: KS statistic and two-tailed p-value.
    """
    # Convert data to a numpy array
    data = np.array(data)

    # Perform the KS test
    d, p_value = stats.kstest(data, "norm", args=(np.mean(data), np.std(data)))

    return d, p_value
