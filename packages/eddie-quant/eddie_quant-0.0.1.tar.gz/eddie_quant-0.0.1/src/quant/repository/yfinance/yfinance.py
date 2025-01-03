from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

import pandas as pd
import yfinance as yf

from quant.common.models.history import History
from quant.common.models.ticker import Ticker


@dataclass
class _HistoryRequest:
    start_date: Optional[str]
    end_date: Optional[str]
    interval: str


class YFinanceRepository:
    def __init__(self):
        pass

    def get_ticker_info(self, ticker: str) -> Ticker:
        ticker = yf.Ticker(ticker)
        ticker_info = ticker.info
        result = Ticker(
            symbol=ticker_info["symbol"],
            exchange=ticker_info["exchange"],
            quote_type=ticker_info["quoteType"],
            short_name=ticker_info["shortName"],
            long_name=ticker_info["longName"],
        )
        return result

    def get_ticker_price_history(self, symbol: str, start_date: Optional[str], end_date: Optional[str],
                                 interval_list: list[str]) -> list[History]:
        ticker = yf.Ticker(symbol)
        ticker.history(start=start_date, end=end_date)
        request_list: list[_HistoryRequest] = []

        for interval in interval_list:
            request = _HistoryRequest(
                start_date=start_date,
                end_date=end_date,
                interval=interval,
            )
            request_list.append(request)

        return self._get_ticker_price_history_internal(symbol=symbol, request_list=request_list)

    def _get_ticker_price_history_internal(self, symbol: str, request_list: list[_HistoryRequest]) -> list[History]:
        result: list[History] = []
        ticker = yf.Ticker(symbol)

        for request in request_list:
            if request is None:
                continue

            if request.start_date is None and request.end_date is None:
                pd_frames = ticker.history(interval=request.interval, period="max")
            else:
                start_date_datetime = pd.to_datetime(request.start_date)
                end_date_datetime = pd.to_datetime(request.end_date)
                pd_frames = ticker.history(interval=request.interval, start=start_date_datetime, end=end_date_datetime)

            if pd_frames is None:
                print(f"pd_frames is None got from request {request}")
                continue

            history_list = pd_frames.apply(self._dataframe_row_to_history, axis=1).tolist()

            for each in history_list:
                each.symbol = symbol
                each.interval = request.interval

            result.extend(history_list)

        result.sort(key=lambda x: x.time, reverse=False)
        return result

    def _dataframe_row_to_history(self, row: pd.Series) -> History:
        return History(
            # symbol=row["symbol"],
            time=row.name,
            # interval=row["interval"],
            open=Decimal(round(row["Open"], 2)),
            high=Decimal(round(row["High"], 2)),
            low=Decimal(round(row["Low"], 2)),
            close=Decimal(round(row["Close"], 2)),
            volume=Decimal(row["Volume"]),
        )
