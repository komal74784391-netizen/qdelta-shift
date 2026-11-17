"""Drift detectors built on top of the streaming quantile sketch."""

from .streaming import P2Quantile


class QuantileDriftDetector:
    def __init__(self, window: int = 512, threshold: float = 0.05):
        self.window = window
        self.threshold = threshold
        self.left = P2Quantile(0.5)
        self.right = P2Quantile(0.5)

    def push(self, value: float) -> bool:
        self.right.update(value)
        return abs(self.right.estimate() - self.left.estimate()) > self.threshold
