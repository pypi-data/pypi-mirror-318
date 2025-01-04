from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING

from typing_extensions import override

from modular_trader.allocation import AllocationTarget
from modular_trader.signal import SignalDirection

from .base import BasePortfolioConstruction

if TYPE_CHECKING:
    from modular_trader.allocation import Allocation
    from modular_trader.context import Context
    from modular_trader.signal import SignalCollection


class EqualWeightPortfolioConstruction(BasePortfolioConstruction):
    """
    Assigns equal weight to all signals. Liquidates positions no longer in signals.
    """

    @override
    def run(self, context: Context, signals: SignalCollection) -> Iterable[Allocation]:
        filtered_signals = [s for s in signals if s.direction == SignalDirection.UP]
        if len(filtered_signals) == 0:
            return []
        w = 1 / len(filtered_signals)
        targets = [AllocationTarget(s.symbol, w) for s in filtered_signals]

        # Liquidate holding symbols, no longer in targets
        signal_symbols = [s.symbol for s in filtered_signals]
        pos_symbols: list[str] = [p.symbol for p in context.engine.get_positions()]
        liqudate_symbols = set(pos_symbols).difference(signal_symbols)
        liquidates = [AllocationTarget(s, 0) for s in liqudate_symbols]

        return [*liquidates, *targets]
