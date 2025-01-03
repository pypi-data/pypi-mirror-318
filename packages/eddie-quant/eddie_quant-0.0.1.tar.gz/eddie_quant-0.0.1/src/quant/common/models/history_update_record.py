import json

from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy import Index
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class HistoryUpdateRecord(Base):
    __tablename__ = 'history_update_record'

    id = Column(Integer, primary_key=True)
    symbol = Column(String(12), nullable=False)
    date = Column(String(10), nullable=False)

    created_at = Column(TIMESTAMP, default=func.current_timestamp())

    def to_dict(self):
        return {
            "id": self.id,
            "symbol": self.symbol,
            "date": self.date,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return json.dumps(self.to_dict(), ensure_ascii=False)


Index('idx_history_symbol', HistoryUpdateRecord.symbol)
Index('idx_history_date', HistoryUpdateRecord.date)
