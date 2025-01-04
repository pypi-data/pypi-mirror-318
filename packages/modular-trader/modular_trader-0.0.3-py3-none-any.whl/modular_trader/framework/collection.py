from pydantic import BaseModel, ConfigDict

from modular_trader.framework.asset_selection.base import BaseAssetSelection
from modular_trader.framework.order_execution.base import BaseOrderExecution
from modular_trader.framework.portfolio_construction.base import (
    BasePortfolioConstruction,
)
from modular_trader.framework.risk_management.base import BaseRiskManagement
from modular_trader.framework.signal_generation.base import BaseSignalGeneration


class FrameworkCollection(BaseModel):
    """Collection of all the components of a framework.

    Contains:
        - asset_selection: Instance of BaseAssetSelection
        - signal_generation: Instance of BaseSignalGeneration
        - portfolio_construction: Instance of BasePortfolioConstruction
        - order_execution: Instance of BaseOrderExecution
        - risk_management: Instance of BaseRiskManagement

    Attributes:
        asset_selection: Instance of BaseAssetSelection
        signal_generation: Instance of BaseSignalGeneration
        portfolio_construction: Instance of BasePortfolioConstruction
        order_execution: Instance of BaseOrderExecution
        risk_management: Instance of BaseRiskManagement
    """

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid", frozen=True)
    asset_selection: BaseAssetSelection
    signal_generation: BaseSignalGeneration
    portfolio_construction: BasePortfolioConstruction
    order_execution: BaseOrderExecution
    risk_management: BaseRiskManagement
