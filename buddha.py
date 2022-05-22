import numpy as np
from PIL import Image


class Buddha:
    def __init__(self) -> None:
        self.paths = None
        self.image = None

    def build(self, iterations: int = 100, n_points: int = 10_000) -> None:
        self.paths = np.zeros((iterations + 1, n_points), dtype=complex)
        self.paths[0, :] = np.random.uniform(-2, 2, n_points) + np.random.uniform(-2, 2, n_points) * 1j

        for i in range(1, iterations + 1):
            z = self.paths[i - 1, :] ** 2 + self.paths[0, :]  # z_{n+1} = z_n^2 + c
            self.paths[i, :] = np.where(np.abs(z) <= 2, z, np.nan)

    def render(self, resolution: (int, int) = (1_000, 1_000), zoom: float = 3.5) -> None:
        if self.paths is None:
            print("You must call Buddha.build() before rendering")
            return

        self.image = np.zeros(resolution, dtype=int)
        escapees = np.isnan(self.paths[-1, :])
        for step in self.paths[:, escapees]:
            step = step[np.isfinite(step)]
            step = (step + 2 + 2j) / 4 * max(resolution)
            ys = step.imag.astype(int)
            xs = step.real.astype(int)
            ys = ys[ys < resolution[0]]
            xs = xs[xs < resolution[1]]
            self.image[ys, xs] += 1
        self.image = 255 * self.image // self.image.max(initial=1)

    def show(self) -> None:
        if self.image is None:
            print("You must call Buddha.render() before showing")
            return

        im = Image.fromarray(self.image, mode="L")
        im.show()

    def save(self, filename: str = "buddhabrot") -> None:
        if self.image is None:
            print("You must call Buddha.render() before saving")
            return

        im = Image.fromarray(self.image, mode="L")
        im.save(filename, format="PNG")
