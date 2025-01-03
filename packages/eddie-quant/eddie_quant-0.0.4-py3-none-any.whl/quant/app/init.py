from quant.app.service import AppService
from quant.common.utils.log import LoggerConfig
from quant.core.service.persist_data_service import PersistentDataService

from quant.repository.postgresql.engine import Engine
from quant.repository.postgresql.history import HistoryRepository
from quant.repository.postgresql.ticker import TickerRepository
from quant.repository.yfinance.yfinance import YFinanceRepository


def init_app_service() -> AppService:
    # log
    LoggerConfig()

    # postgresql
    engine = Engine()
    ticker_repository = TickerRepository(engine)
    history_repository = HistoryRepository(engine)

    # yfinance
    yfinance_repository = YFinanceRepository()

    # service
    ticker_service = PersistentDataService(yfinance_repository, ticker_repository, history_repository)

    # app
    app_service = AppService(ticker_service)

    return app_service
