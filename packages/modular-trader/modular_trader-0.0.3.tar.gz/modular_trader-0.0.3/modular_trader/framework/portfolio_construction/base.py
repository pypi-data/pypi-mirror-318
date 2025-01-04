from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from modular_trader.allocation import Allocation
    from modular_trader.context import Context
    from modular_trader.signal import SignalCollection


class BasePortfolioConstruction(ABC):
    """Base class for portfolio construction.

    This class defines the interface for all portfolio construction strategies.

    The `__call__` method is called by the framework to construct the portfolio.
    It is expected to clear the current allocations and add the new allocations.

    The `run` method is called by `__call__` to perform the portfolio construction.
    It must be implemented by subclasses to return an iterable of `Allocation` objects.
    """

    def __call__(self, context: Context, signals: SignalCollection) -> Any:
        allocations: Iterable[Allocation] = self.run(context, signals) or []
        context.allocations.clear()  # clearing old before adding new
        context.allocations.add(allocations)

    @abstractmethod
    def run(self, context: Context, signals: SignalCollection) -> Iterable[Allocation]:
        """Must be implemented by subclasses.

        Called by `__call__` to perform portfolio construction.
        """
        pass
