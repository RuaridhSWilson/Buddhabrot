import numpy as np
from PIL import Image


class Buddha:
    def __init__(self) -> None:
        self.paths = None
        self.image = None

    def build(self, iterations: int = 100, n_points: int = 10_000) -> None:
        self.paths = np.zeros((iterations + 1, n_points), dtype=complex)
        c = np.random.uniform(-2, 2, n_points) + np.random.uniform(-2, 2, n_points) * 1j
        self.paths[0, :] = np.where(np.abs(c) <= 2, c, np.nan)

        for i in range(1, iterations + 1):
            z = self.paths[i - 1, :] ** 2 + self.paths[0, :]  # z_{n+1} = z_n^2 + c
            self.paths[i, :] = np.where(np.abs(z) <= 2, z, np.nan)

    def save_paths(self, filename: str = "buddha_paths") -> None:
        np.save(filename, self.paths)

    def render(self, resolution: (int, int) = (1_000, 1_000), zoom: float = 3.5) -> None:
        if self.paths is None:
            print("You must call Buddha.build() before rendering")
            return

        self.image = np.zeros(resolution, dtype=int)
        escapees = np.isnan(self.paths[-1, :])
        for step in self.paths[:, escapees]:
            step = step[np.isfinite(step)]
            if step.size == 0:
                break
            step = (step + 2 + 2j) / 4 * max(resolution)
            ys = step.imag.astype(int)
            xs = step.real.astype(int)
            ys = ys[ys < resolution[0]]
            xs = xs[xs < resolution[1]]
            np.add.at(self.image, (xs, ys), 1)
        self.image = 255 * self.image // self.image.max(initial=1)
        self.image = np.uint8(self.image)

    def save_render(self, filename: str = "buddha_render") -> None:
        np.save(filename, self.image)

    def show(self) -> None:
        if self.image is None:
            print("You must call Buddha.render() before showing")
            return
        im = Image.fromarray(self.image, mode="L")
        im.show()

    def export(self, filename: str = "buddhabrot") -> None:
        if self.image is None:
            print("You must call Buddha.render() before exporting")
            return
        im = Image.fromarray(self.image, mode="L")
        im.save(filename, format="PNG")
