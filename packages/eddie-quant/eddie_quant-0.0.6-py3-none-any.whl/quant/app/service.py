from typing import Optional

from loguru import logger

from quant.common.consts.time import Interval
from quant.common.models.history import History
from quant.common.models.ticker import Ticker
from quant.core.service.data.persist_data_service import PersistentDataService


class AppService:
    def __init__(self, persistent_data_service: PersistentDataService):
        self.__persistent_data_service = persistent_data_service

    def add_ticker_info(self, symbols: list[str]) -> list[str]:
        """
        Add
        :param symbols:
        :return: failed symbols
        """
        failed_symbols = []
        for symbol in symbols:
            try:
                self.__persistent_data_service.add_ticker_data_to_db(symbol)
            except BaseException as e:
                failed_symbols.append(symbol)
                logger.warning(f"failed adding {symbol} to db")

        return failed_symbols

    def get_ticker_info(self, symbols: Optional[list[str]]) -> list[Ticker]:
        if symbols is None:
            return self.__persistent_data_service.get_all_ticker_data_from_db()
        else:
            return self.__persistent_data_service.get_tickers_data_from_db(symbols)

    def update_latest_history_data(self, symbols: list[str]):
        for symbol in symbols:
            self.__persistent_data_service.update_latest_ticker_history_to_db(symbol=symbol)

    def update_full_history_data(self, symbols: list[str]):
        for symbol in symbols:
            self.__persistent_data_service.update_full_ticker_history_to_db(symbol=symbol)

    def get_history_latest_date(self, symbol: str) -> Optional[str]:
        return self.__persistent_data_service.get_history_latest_date(symbol)

    def get_history_data(self, symbol: str, start_date: Optional[str], end_date: Optional[str],
                         interval: Optional[Interval]) -> list[History]:
        """
        Get ticker history data from persistent data service (database)
        :param symbol : str ticker symbol
        :param start_date: str '2025-01-02', inclusive
        :param end_date: str '2025-01-03', exclusive
        :param interval: str interval
        :returns list[History] list of history data
        """
        return self.__persistent_data_service.get_history_by_symbol(symbol=symbol, start_date=start_date,
                                                                    end_date=end_date, interval=str(interval.value))
