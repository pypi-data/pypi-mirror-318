from sqlalchemy.dialects.postgresql import insert

from quant.common.models.history import History
from quant.repository.postgresql.engine import Engine


class HistoryRepository:
    def __init__(self, engine: Engine):
        self.__engine = engine

    def insert(self, price_record: History):
        session = self.__engine.session()

        try:
            session.add(price_record)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error inserting {price_record}: {e}")
        finally:
            session.close()

    def m_insert(self, price_records: list[History]):
        session = self.__engine.session()

        try:
            for record in price_records:
                stmt = insert(History).values(
                    symbol=record.symbol,
                    time=record.time,
                    interval=record.interval,
                    open=record.open,
                    high=record.high,
                    low=record.low,
                    close=record.close,
                    volume=record.volume
                )

                stmt = stmt.on_conflict_do_nothing(index_elements=['symbol', 'time', 'interval'])
                session.execute(stmt)

            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error inserting records: {e}")
        finally:
            session.close()
