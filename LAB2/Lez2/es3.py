import numpy as np



rng = np.random.default_rng(42)


arr = rng.random((10, 3))

closest_idx = np.abs(arr - 0.5).argmin(axis=1)

result = arr[np.arange(10), closest_idx]
print(result)
