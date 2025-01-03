from quant.common.consts.time import Interval
from quant.repository.postgresql.history import HistoryRepository
from quant.repository.postgresql.ticker import TickerRepository
from quant.repository.yfinance.yfinance import YFinanceRepository


class PersistentDataService:
    def __init__(self, yfinance_repository: YFinanceRepository, ticker_repository: TickerRepository,
                 history_repository: HistoryRepository):
        self.__yfinance_repository = yfinance_repository
        self.__ticker_repository = ticker_repository
        self.__history_repository = history_repository

    def update_ticker_data_to_db(self, symbol: str):
        if len(symbol) < 1:
            raise ValueError("symbol is empty")

        try:
            existing_ticker_record = self.__ticker_repository.get(symbol=symbol)
            if existing_ticker_record is None:
                ticker = self.__yfinance_repository.get_ticker_info(symbol)
                self.__ticker_repository.insert(ticker)
            else:
                print(f"no record insert, ticker record already exists {existing_ticker_record} for symbol {symbol}")
        except Exception as e:
            raise BaseException(f"failed to get ticker info for {symbol}: {e}")

    def update_ticker_history_to_db(self, symbol: str):
        if len(symbol) < 1:
            raise ValueError("symbol is empty")

        try:
            self.__ticker_repository.get(symbol)
        except Exception as e:
            raise BaseException(f"failed to get ticker info for {symbol}: {e}")

        interval_list = [member.value for member in Interval]

        history_list = self.__yfinance_repository.get_ticker_price_history(symbol=symbol, start_date=None,
                                                                           end_date=None,
                                                                           interval_list=interval_list)
        try:
            self.__history_repository.m_insert(history_list)
        except Exception as e:
            raise BaseException(f"failed to insert history data {history_list} for {symbol}: {e}")
