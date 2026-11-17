"""Streaming quantile estimators used by the qdelta monitor."""

import numpy as np


class P2Quantile:
    def __init__(self, q: float = 0.5):
        self.q = q
        self.buffer = []

    def update(self, value: float) -> None:
        self.buffer.append(value)

    def estimate(self) -> float:
        return float(np.quantile(self.buffer, self.q)) if self.buffer else 0.0
