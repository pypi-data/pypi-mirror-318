from typing import List

from quant.core.service.persist_data_service import PersistentDataService


class AppService:
    def __init__(self, persistent_data_service: PersistentDataService):
        self.__persistent_data_service = persistent_data_service

    def update_ticker_info(self, symbols: List[str]):
        for symbol in symbols:
            self.__persistent_data_service.update_ticker_data_to_db(symbol)

    def update_history_data(self, symbols: List[str]):
        for symbol in symbols:
            self.__persistent_data_service.update_ticker_history_to_db(symbol)
