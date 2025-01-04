<a id="readme-top"></a>

# Modular-Trader: A Flexible Algorithmic Trading Framework

![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge)

**Important Note**: This project is currently undergoing substantial updates. Significant changes to existing functions and classes are anticipated, and compatibility with the current version may be affected.

<!-- ![logo](docs/source/modular-trader-logo.svg) -->
![logo](https://raw.githubusercontent.com/kfuangsung/modular-trader/refs/heads/main/docs/source/_static/modular-trader-logo.svg)



## About The Project
<!-- ![flow](docs/source/modular-trader-flow.svg) -->
![flow](https://raw.githubusercontent.com/kfuangsung/modular-trader/refs/heads/main/docs/source/_static/modular-trader-flow.svg)



**Modular Trader** is a Python-based framework for algorithmic trading, designed with a strong emphasis on **modularity** and **flexibility**. It provides a comprehensive solution as a set of building blocks for the live deployment of algorithmic trading strategies.

The framework is organized into five core modules, each addressing a critical aspect of the trading process:

- **Asset Selection**: Identifies and selects the assets to include in the trading universe.
- **Signal Generation**: Produces trading signals based on various strategies and indicators.
- **Portfolio Construction**: Allocates portfolio weights based on the generated signals.
- **Risk Management**: Adjusts portfolio allocations to mitigate and manage risk effectively
- **Order Execution**: Manages the execution of buy/sell orders in the market.

### Built-in Models 

#### Asset Selection 
- Manual

#### Signal Generation
- Constant

#### Portfolio Builder 
- EqualWeight
- ThresholdDeviation

#### Order Execution
- Instant

#### Risk Management
- FixedStopLoss


### Supported Brokerages

- [Alpaca](https://alpaca.markets/)

**Important Note**: We are not affiliated, associated, authorized, endorsed by, or in any way officially connected with Alpaca Securities LLC, or any of its subsidiaries or its affiliates. The official Alpaca Securities LLC website can be found at https://alpaca.markets/.


## Getting Started

### Installation
```bash
pip install modular-trader
```



## Usage 
```python
from dotenv import load_dotenv
from modular_trader.common.enums import TradingMode
from modular_trader.engine import AlpacaEngine
from modular_trader.framework import FrameworkCollection
from modular_trader.framework.asset_selection import ManualAssetSelection
from modular_trader.framework.order_execution import InstantOrderExecution
from modular_trader.framework.portfolio_construction import EqualWeightPortfolioConstruction
from modular_trader.framework.risk_management import NullRiskManagement
from modular_trader.framework.signal_generation import ConstantSignalGeneration
from modular_trader.trader import AlpacaTrader

# set Alpaca Token  as environment variable
# create `.env` file then add
# ALPACA_API_KEY=xxxxxxxx
# ALPACA_SECRET_KEY=xxxxxxx
load_dotenv()

# Equally weighted portfolio
# with Instant rebalancing
symbols = ["SPY", "QQQ", "GLD"]
framework = FrameworkCollection(
    asset_selection=ManualAssetSelection(symbols=symbols),
    signal_generation=ConstantSignalGeneration(),
    portfolio_construction=EqualWeightPortfolioConstruction(),
    order_execution=InstantOrderExecution(),
    risk_management=NullRiskManagement(),
)

# using Paper portfolio
engine = AlpacaEngine(mode=TradingMode.PAPER)

trader = AlpacaTrader(
    engine=engine,
    framework=framework,
    subscription_symbols=symbols,
)

trader.run()
```



## License 
Distributed under the MIT License. See [`LICENSE`](https://github.com/kfuangsung/modular-trader/blob/main/LICENSE) for more information.


## Maintainers

[Modular Trader]() is currently maintained by [kfuangsung](https://github.com/kfuangsung) (kachain.f@outlook.com).

**Important Note**: We do not provide technical support, or consulting and do not answer personal questions via email.


## Acknowledgments
- [alpaca-py](https://github.com/alpacahq/alpaca-py): An official Python SDK for Alpaca APIs.


## Disclaimer 
Authors and contributors of Modular-Trader cannot be held responsible for possible losses or other damage. Consequently, no claims for damages can be asserted. Please also note that trading has a certain addictive potential. If you find yourself at risk, please seek professional help.