import numpy as np


class Buddha:
    def __init__(self) -> None:
        self.paths = None

    def build(self, iterations: int = 100, n_points: int = 10_000) -> None:
        self.paths = np.zeros((iterations + 1, n_points), dtype=complex)
        self.paths[0, :] = np.random.uniform(-2, 2, n_points) + np.random.uniform(-2, 2, n_points) * 1j

        for i in range(1, iterations + 1):
            z = self.paths[i - 1, :] ** 2 + self.paths[0, :]  # z_{n+1} = z_n^2 + c
            self.paths[i, :] = np.where(np.abs(z) <= 2, z, np.nan)
        return

    def render(self, resolution: (int, int) = (1_000, 1_000), zoom: float = 3.5):
        return
