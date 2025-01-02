__all__ = [
    "ExponentialMovingAverage",
    "Maximum",
    "Minimum",
    "MovingAverageConvergenceDivergence",
    "SimpleMovingAverage",
]

class ExponentialMovingAverage:
    def __init__(self, period: int) -> None:
        """Exponential moving average."""

    def period(self) -> int:
        """Return the number of periods."""

    def next(self, input: float) -> float:
        """Calculate the exponential moving average of the current periods."""

    def reset(self) -> None:
        """Reset the current calculations."""

class Maximum:
    def __init__(self, period: int) -> None:
        """Create a new maximum indicator."""

    def period(self) -> int:
        """Return the number of periods."""

    def next(self, input: float) -> float:
        """Calculate the maximum of the current periods."""

    def reset(self) -> None:
        """Reset the current calculations."""

class Minimum:
    def __init__(self, period: int) -> None:
        """Create a minimum indicator."""

    def period(self) -> int:
        """Return the number of periods."""

    def next(self, input: float) -> float:
        """Calculate the minimm of the current periods."""

    def reset(self) -> None:
        """Reset the current calculations."""

class MovingAverageConvergenceDivergence:
    def __init__(self, long_period: int, short_period: int) -> None:
        """Moving average convergence divergence."""

    def next(self, input: float) -> tuple[float, float, float]:
        """Calculate the moving average convergence divergence of the current periods."""

    def reset(self) -> None:
        """Reset the current calculations."""

class SimpleMovingAverage:
    def __init__(self, period: int) -> None:
        """Create a simple moving average indicator."""

    def period(self) -> int:
        """Return the number of periods."""

    def next(self, input: float) -> float:
        """Calculate the simple moving average of the current periods."""

    def reset(self) -> None:
        """Reset the current calculations."""
