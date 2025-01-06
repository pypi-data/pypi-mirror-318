from datetime import datetime, timedelta
from typing import Optional

from loguru import logger

from quant.common.consts.time import Interval, TimeConfig
from quant.common.models.history import History
from quant.common.models.ticker import Ticker
from quant.repository.postgresql.history import HistoryRepository
from quant.repository.postgresql.ticker import TickerRepository
from quant.repository.yfinance.yfinance import YFinanceRepository


class PersistentDataService:
    def __init__(self, yfinance_repository: YFinanceRepository, ticker_repository: TickerRepository,
                 history_repository: HistoryRepository):
        self.__yfinance_repository = yfinance_repository
        self.__ticker_repository = ticker_repository
        self.__history_repository = history_repository

    def add_ticker_data_to_db(self, symbol: str):
        if len(symbol) < 1:
            raise ValueError("symbol is empty")

        try:
            existing_ticker_record = self.get_ticker_data_from_db(symbol)
            if existing_ticker_record is None:
                ticker = self.__yfinance_repository.get_ticker_info(symbol)
                self.__ticker_repository.insert(ticker)
            else:
                logger.warning(
                    f"no record insert, ticker record already exists {existing_ticker_record} for symbol {symbol}")
        except Exception as e:
            raise BaseException(f"failed to add ticker info for {symbol}: {e}")

    def get_all_ticker_data_from_db(self) -> list[Ticker]:
        return self.__ticker_repository.get_all()

    def get_tickers_data_from_db(self, symbols: list[str]) -> list[Ticker]:
        return self.__ticker_repository.get_by_symbols(symbols)

    def get_ticker_data_from_db(self, symbol: str) -> Optional[Ticker]:
        try:
            return self.__ticker_repository.get(symbol=symbol)
        except Exception as e:
            logger.error(f"failed to get ticker info for {symbol}: {e}")
            return None

    def update_ticker_history_to_db(self, symbol: str, start_date: Optional[str], end_date: Optional[str]):
        """
        Update historical price history from Yahoo Finance to db
        :param symbol: str, such as 'AAPL'
        :param start_date: str, YYYY-MM-DD, inclusive, if start date is none, will update all days before end_date (inclusive)
        :param end_date: str, YYYY-MM-DD, exclusive, if end date is none, will update all days after start_date else
                                        if both start_date and end_date are none, will update all days before today (include today)
        """

        if len(symbol) < 1:
            raise ValueError("symbol is empty")

        try:
            self.__ticker_repository.get(symbol)
        except Exception as e:
            raise BaseException(f"failed to get ticker info for {symbol}: {e}")

        interval_list = [member.value for member in Interval]
        history_list = self.__yfinance_repository.get_ticker_price_history(symbol=symbol, start_date=start_date,
                                                                           end_date=end_date,
                                                                           interval_list=interval_list)

        try:
            self.__history_repository.m_insert(history_list)
        except Exception as e:
            raise BaseException(f"failed to insert history data {history_list} for {symbol}: {e}")

    def update_full_ticker_history_to_db(self, symbol: str):
        return self.update_ticker_history_to_db(symbol, start_date=None, end_date=None)

    def update_latest_ticker_history_to_db(self, symbol: str):
        try:
            latest_date = self.get_history_latest_date(symbol)
            if latest_date is None:
                raise Exception(f"no history data for {symbol}")
        except Exception as e:
            logger.info(f"failed to get history data for {symbol}: {e}")
            raise BaseException(f"failed to get latest date for {symbol}: {e}")

        return self.update_ticker_history_to_db(symbol, start_date=latest_date, end_date=None)

    def get_history_by_symbol(self, symbol: str, start_date: Optional[str], end_date: Optional[str],
                              interval: str) -> list[History]:

        if start_date is None and end_date is None:
            return self.__history_repository.get_all(symbol)
        if start_date is None:
            start_date = TimeConfig.DEFAULT_START_DATE
        if end_date is None:
            current_time = datetime.now(TimeConfig.DEFAULT_TIMEZONE)
            end_datetime = current_time + timedelta(hours=24)  # add one day to include today's data
            end_date = end_datetime.strftime(TimeConfig.DEFAULT_DATE_FORMAT)

        records = self.__history_repository.get_by_date(symbol=symbol, start_date=start_date, end_date=end_date)
        if interval is None:
            return records

        return list(filter(lambda r: r.interval == interval, records))

    def get_history_latest_date(self, symbol: str) -> Optional[str]:
        latest_data = self.__history_repository.get_latest(symbol=symbol)
        if latest_data is None:
            return None

        return latest_data.time.astimezone(TimeConfig.DEFAULT_TIMEZONE).strftime(
            TimeConfig.DEFAULT_DATE_FORMAT)
