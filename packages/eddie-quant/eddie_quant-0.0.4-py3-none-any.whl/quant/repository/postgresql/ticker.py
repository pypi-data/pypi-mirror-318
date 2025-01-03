from typing import cast

from quant.common.models.ticker import Ticker
from quant.repository.postgresql.engine import Engine


class TickerRepository:
    def __init__(self, engine: Engine):
        self.__engine = engine

    def insert(self, ticker: Ticker):
        session = self.__engine.session()

        try:
            session.add(ticker)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error inserting {ticker}: {e}")
        finally:
            session.close()

    def m_insert(self, tickers: list[Ticker]):
        session = self.__engine.session()

        try:
            session.add_all(tickers)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error inserting {tickers}: {e}")
        finally:
            session.close()

    def get(self, symbol: str) -> Ticker:
        result = Ticker()
        session = self.__engine.session()

        try:
            result = session.query(Ticker).filter_by(symbol=symbol).first()
        except Exception as e:
            session.rollback()
            print(f"Error query ticker with symbol {symbol} : {e}")
        finally:
            session.close()

        if result is None:
            raise Exception(f"Symbol {symbol} not found.")

        return cast(Ticker, result)
