import pandas as pd
from urllib.parse import urlencode
from datetime import datetime, timedelta, timezone
import pytz
import aiohttp
import asyncio
import httpx
from typing import List
import logging
from fudstop.apis.polygonio.models.option_models.universal_snapshot import UniversalOptionSnapshot
from fudstop.apis.webull.trade_models.analyst_ratings import Analysis
from fudstop.apis.webull.trade_models.stock_quote import MultiQuote
from fudstop.apis.webull.trade_models.capital_flow import CapitalFlow, CapitalFlowHistory
from fudstop.apis.webull.trade_models.deals import Deals
from fudstop.apis.webull.trade_models.cost_distribution import CostDistribution, NewCostDist
from fudstop.apis.webull.trade_models.etf_holdings import ETFHoldings
from fudstop.apis.webull.trade_models.institutional_holdings import InstitutionHolding, InstitutionStat
from fudstop.apis.webull.trade_models.financials import BalanceSheet, FinancialStatement, CashFlow
from fudstop.apis.webull.trade_models.news import NewsItem
from fudstop.apis.webull.trade_models.forecast_evaluator import ForecastEvaluator
from fudstop.apis.webull.trade_models.short_interest import ShortInterest
from fudstop.apis.webull.webull_option_screener import WebullOptionScreener
from fudstop.apis.webull.trade_models.volume_analysis import WebullVolAnalysis
from fudstop.apis.webull.trade_models.ticker_query import WebullStockData
from fudstop.apis.webull.trade_models.analyst_ratings import Analysis
from fudstop.apis.webull.trade_models.price_streamer import PriceStreamer
from fudstop.apis.webull.trade_models.company_brief import CompanyBrief, Executives, Sectors
from fudstop.apis.webull.trade_models.order_flow import OrderFlow
import asyncio
import aiohttp
import os
from dotenv import load_dotenv
load_dotenv()
class UltimateSDK:
    def __init__(self):
    # ---------------------------------------------------------------
    # SINGLE-TICKER METHODS (as you already have them)
    # ---------------------------------------------------------------


        self.api_key = os.environ.get('YOUR_POLYGON_KEY')
        self.scalar_tickers = ['SPX', 'VIX', 'OSTK', 'XSP', 'NDX', 'MXEF']
        self.today = datetime.now().strftime('%Y-%m-%d')
        self.semaphore = asyncio.Semaphore(10)
        self.yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        self.tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        self.thirty_days_ago = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        self.thirty_days_from_now = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')
        self.fifteen_days_ago = (datetime.now() - timedelta(days=15)).strftime('%Y-%m-%d')
        self.fifteen_days_from_now = (datetime.now() + timedelta(days=15)).strftime('%Y-%m-%d')
        self.eight_days_from_now = (datetime.now() + timedelta(days=8)).strftime('%Y-%m-%d')
        self.eight_days_ago = (datetime.now() - timedelta(days=8)).strftime('%Y-%m-%d')
        self.timeframes = ['m1','m5', 'm10', 'm15', 'm20', 'm30', 'm60', 'm120', 'm240', 'd1']
        self.now_timestamp_int = int(datetime.now(timezone.utc).timestamp())
        self.day = int(86400)
        self.ticker_df = pd.read_csv('files/ticker_csv.csv')
        self.id = 15765933
        self.ticker_to_id_map = dict(zip(self.ticker_df['ticker'], self.ticker_df['id']))

    async def get_analyst_ratings(self, symbol: str):
        try:
            ticker_id = self.ticker_to_id_map.get(symbol)
            endpoint = f"https://quotes-gw.webullfintech.com/api/information/securities/analysis?tickerId={ticker_id}"
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    if resp.status == 200:
                        datas = await resp.json()
                        return Analysis(datas)
        except Exception as e:
            print(e)
        return None

    async def get_short_interest(self, symbol: str):
        try:
            ticker_id = self.ticker_to_id_map.get(symbol)
            if not ticker_id:
                raise ValueError(f"Ticker {symbol} not found in ticker_to_id_map.")

            endpoint = f"https://quotes-gw.webullfintech.com/api/information/brief/shortInterest?tickerId={ticker_id}"
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    if resp.status == 200:
                        datas = await resp.json()
                        return ShortInterest(datas)
        except Exception as e:
            print(f"Error: {e}")
        return None

    async def institutional_holding(self, symbol: str):
        try:
            ticker_id = self.ticker_to_id_map.get(symbol)
            endpoint = f"https://quotes-gw.webullfintech.com/api/information/stock/getInstitutionalHolding?tickerId={ticker_id}"
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    if resp.status == 200:
                        datas = await resp.json()
                        return InstitutionStat(datas)
        except Exception as e:
            print(e)
        return None

    async def volume_analysis(self, symbol: str):
        try:
            ticker_id = self.ticker_to_id_map.get(symbol)
            endpoint = f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/stat?count=10&tickerId={ticker_id}&type=0"
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    if resp.status == 200:
                        datas = await resp.json()
                        return WebullVolAnalysis(datas, symbol)
        except Exception as e:
            print(e)
        return None

    async def new_cost_dist(self, symbol: str, start_date: str, end_date: str):
        """Returns list"""
        try:
            ticker_id = self.ticker_to_id_map.get(symbol)
            endpoint = (
                f"https://quotes-gw.webullfintech.com/api/quotes/chip/query?"
                f"tickerId={ticker_id}&startDate={start_date}&endDate={end_date}"
            )
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        data = data['data']
                        return NewCostDist(data, symbol)
        except Exception as e:
            print(e)
        return None

    # ---------------------------------------------------------------
    # MULTI-TICKER METHODS (concurrent versions)
    # ---------------------------------------------------------------

    async def institutional_holdings_for_tickers(
        self, 
        tickers: list[str]
    ) -> dict[str, InstitutionStat | None]:
        """
        Fetch institutional holding for multiple tickers concurrently.
        Returns a dict: { ticker: InstitutionStat object (or None) }
        """
        tasks = [
            asyncio.create_task(self.institutional_holding(ticker))
            for ticker in tickers
        ]
        results = await asyncio.gather(*tasks)
        return dict(zip(tickers, results))

    async def short_interest_for_tickers(
        self, 
        tickers: list[str]
    ) -> dict[str, ShortInterest | None]:
        """
        Fetch short interest for multiple tickers concurrently.
        Returns a dict: { ticker: ShortInterest object (or None) }
        """
        tasks = [
            asyncio.create_task(self.get_short_interest(ticker))
            for ticker in tickers
        ]
        results = await asyncio.gather(*tasks)
        return dict(zip(tickers, results))

    async def analyst_ratings_for_tickers(
        self, 
        tickers: list[str]
    ) -> dict[str, Analysis | None]:
        """
        Fetch analyst ratings for multiple tickers concurrently.
        Returns a dict: { ticker: Analysis object (or None) }
        """
        tasks = [
            asyncio.create_task(self.get_analyst_ratings(ticker))
            for ticker in tickers
        ]
        results = await asyncio.gather(*tasks)
        return dict(zip(tickers, results))

    async def volume_analysis_for_tickers(
        self, 
        tickers: list[str]
    ) -> dict[str, WebullVolAnalysis | None]:
        """
        Fetch volume analysis for multiple tickers concurrently.
        Returns a dict: { ticker: WebullVolAnalysis object (or None) }
        """
        tasks = [
            asyncio.create_task(self.volume_analysis(ticker))
            for ticker in tickers
        ]
        results = await asyncio.gather(*tasks)
        return dict(zip(tickers, results))

    async def new_cost_dist_for_tickers(
        self, 
        tickers: list[str], 
        start_date: str, 
        end_date: str
    ) -> dict[str, NewCostDist | None]:
        """
        Fetch new cost dist for multiple tickers concurrently (requires start_date & end_date).
        Returns a dict: { ticker: NewCostDist object (or None) }
        """
        tasks = [
            asyncio.create_task(self.new_cost_dist(ticker, start_date, end_date))
            for ticker in tickers
        ]
        results = await asyncio.gather(*tasks)
        return dict(zip(tickers, results))

    async def _news_single(self, session: httpx.AsyncClient, symbol: str, pageSize: str, headers) -> "NewsItem | None":
        """
        Private helper for fetching news for a single ticker using an existing session.
        """
        try:
            if not headers:
                raise ValueError("Headers are required but not provided.")

            ticker_id = self.ticker_to_id_map.get(symbol)
            if not ticker_id:
                raise ValueError(f"Ticker {symbol} not found in ticker_to_id_map.")

            endpoint = (
                "https://nacomm.webullfintech.com/api/information/news/"
                f"tickerNews?tickerId={ticker_id}&currentNewsId=0&pageSize={pageSize}"
            )
            # session is already created by the caller
            response = await session.get(endpoint)
            if response.status_code == 200:
                datas = response.json()
                return NewsItem(datas)  # your existing data class
            else:
                raise Exception(f"Failed to fetch news data: {response.status_code}")
        except Exception as e:
            print(f"Error in news: {symbol}, {e}")
            return None

    async def _company_brief_single(self, session: httpx.AsyncClient, symbol: str) -> tuple | None:
        """
        Private helper to fetch a company's brief for a single ticker.
        Returns (CompanyBrief, Sectors, Executives) or None.
        """
        try:
            ticker_id = self.ticker_to_id_map.get(symbol)
            if not ticker_id:
                raise ValueError(f"Ticker {symbol} not found.")

            endpoint = f"https://quotes-gw.webullfintech.com/api/information/stock/brief?tickerId={ticker_id}"
            resp = await session.get(endpoint)
            if resp.status_code != 200:
                raise Exception(f"HTTP error: {resp.status_code}")

            datas = resp.json()
            # Your existing data classes
            companyBrief = CompanyBrief(datas["companyBrief"])
            sectors = Sectors(datas["sectors"])
            executives = Executives(datas["executives"])
            return (companyBrief, sectors, executives)
        except Exception as e:
            print(f"Error in company_brief: {symbol}, {e}")
            return None

    async def _balance_sheet_single(self, session: httpx.AsyncClient, symbol: str, limit: str) -> "BalanceSheet | None":
        try:
            ticker_id = self.ticker_to_id_map.get(symbol)
            if not ticker_id:
                raise ValueError(f"Ticker {symbol} not found.")

            endpoint = (
                "https://quotes-gw.webullfintech.com/api/information/financial/"
                f"balancesheet?tickerId={ticker_id}&type=101&fiscalPeriod=0&limit={limit}"
            )
            resp = await session.get(endpoint)
            if resp.status_code == 200:
                datas = resp.json()
                return BalanceSheet(datas)
        except Exception as e:
            print(f"Error in balance_sheet: {symbol}, {e}")
        return None

    async def _cash_flow_single(self, session: httpx.AsyncClient, symbol: str, limit: str) -> "CashFlow | None":
        try:
            ticker_id = self.ticker_to_id_map.get(symbol)
            if not ticker_id:
                raise ValueError(f"Ticker {symbol} not found.")

            endpoint = (
                "https://quotes-gw.webullfintech.com/api/information/financial/"
                f"cashflow?tickerId={ticker_id}&type=102&fiscalPeriod=1,2,3,4&limit={limit}"
            )
            resp = await session.get(endpoint)
            if resp.status_code == 200:
                datas = resp.json()
                return CashFlow(datas)
        except Exception as e:
            print(f"Error in cash_flow: {symbol}, {e}")
        return None

    async def _income_statement_single(self, session: httpx.AsyncClient, symbol: str, limit: str) -> "FinancialStatement | None":
        try:
            ticker_id = self.ticker_to_id_map.get(symbol)
            if not ticker_id:
                raise ValueError(f"Ticker {symbol} not found.")

            endpoint = (
                "https://quotes-gw.webullfintech.com/api/information/financial/"
                f"incomestatement?tickerId={ticker_id}&type=102&fiscalPeriod=1,2,3,4&limit={limit}"
            )
            resp = await session.get(endpoint)
            if resp.status_code == 200:
                datas = resp.json()
                return FinancialStatement(datas)
        except Exception as e:
            print(f"Error in income_statement: {symbol}, {e}")
        return None

    async def _order_flow_single(self, session: httpx.AsyncClient, symbol: str, headers, flow_type: str, count: str) -> "OrderFlow | None":
        try:
            ticker_id = self.ticker_to_id_map.get(symbol)
            if not ticker_id:
                raise ValueError(f"Ticker {symbol} not found.")

            endpoint = (
                "https://quotes-gw.webullfintech.com/api/stock/capitalflow/stat?"
                f"count={count}&tickerId={ticker_id}&type={flow_type}"
            )
            resp = await session.get(endpoint)
            if resp.status_code == 200:
                data = resp.json()
                return OrderFlow(data)
            else:
                raise Exception(f"Failed to fetch order flow data. HTTP Status: {resp.status_code}")
        except Exception as e:
            print(f"Error in order_flow: {symbol}, {e}")
            return None

    async def _capital_flow_single(self, session: httpx.AsyncClient, symbol: str) -> tuple["CapitalFlow | None", "CapitalFlowHistory | None"]:
        try:
            ticker_id = self.ticker_to_id_map.get(symbol)
            if not ticker_id:
                raise ValueError(f"Ticker {symbol} not found.")

            endpoint = (
                "https://quotes-gw.webullfintech.com/api/stock/capitalflow/"
                f"ticker?tickerId={ticker_id}&showHis=true"
            )
            resp = await session.get(endpoint)
            resp.raise_for_status()
            datas = resp.json()

            latest = datas.get("latest", {})
            historical = datas.get("historical", [])

            dates = [i.get("date") for i in historical]
            historical_items = [i.get("item") for i in historical]
            latest_item = latest.get("item", {})

            data = CapitalFlow(latest_item, ticker=symbol)
            history = CapitalFlowHistory(historical_items, dates)
            return data, history
        except httpx.RequestError as req_err:
            print(f"Request error for {symbol}: {req_err}")
        except httpx.HTTPStatusError as http_err:
            print(f"HTTP status error for {symbol}: {http_err}")
        except Exception as e:
            print(f"An unexpected error occurred: {symbol}, {e}")

        return None, None

    async def _etf_holdings_single(self, session: httpx.AsyncClient, symbol: str, pageSize: str) -> "ETFHoldings | None":
        try:
            ticker_id = self.ticker_to_id_map.get(symbol)
            if not ticker_id:
                raise ValueError(f"Ticker {symbol} not found.")

            endpoint = (
                "https://quotes-gw.webullfintech.com/api/information/"
                f"company/queryEtfList?tickerId={ticker_id}&pageIndex=1&pageSize={pageSize}"
            )
            resp = await session.get(endpoint)
            if resp.status_code == 200:
                datas = resp.json()
                return ETFHoldings(datas)
        except Exception as e:
            print(f"Error in etf_holdings: {symbol}, {e}")
        return None

    # -------------------------------------------
    # "for_tickers" methods (concurrent)
    # -------------------------------------------

    async def news_for_tickers(
        self, 
        tickers: list[str], 
        pageSize: str = "100", 
        headers=None
    ) -> dict[str, "NewsItem | None"]:
        """
        Fetch news for multiple tickers concurrently using a single session.
        Returns a dict {ticker: NewsItem or None}.
        """
        async with httpx.AsyncClient(headers=headers) as session:
            tasks = [
                asyncio.create_task(self._news_single(session, sym, pageSize, headers))
                for sym in tickers
            ]
            results = await asyncio.gather(*tasks)
        return dict(zip(tickers, results))

    async def company_brief_for_tickers(
        self, 
        tickers: list[str]
    ) -> dict[str, tuple | None]:
        """
        Fetch company briefs for multiple tickers concurrently.
        Returns {ticker: (companyBrief, sectors, executives) or None}.
        """
        async with httpx.AsyncClient() as session:
            tasks = [
                asyncio.create_task(self._company_brief_single(session, sym))
                for sym in tickers
            ]
            results = await asyncio.gather(*tasks)
        return dict(zip(tickers, results))

    async def balance_sheet_for_tickers(
        self, 
        tickers: list[str], 
        limit: str = "11"
    ) -> dict[str, "BalanceSheet | None"]:
        """
        Fetch balance sheets for multiple tickers concurrently.
        Returns {ticker: BalanceSheet or None}.
        """
        async with httpx.AsyncClient() as session:
            tasks = [
                asyncio.create_task(self._balance_sheet_single(session, sym, limit))
                for sym in tickers
            ]
            results = await asyncio.gather(*tasks)
        return dict(zip(tickers, results))

    async def cash_flow_for_tickers(
        self, 
        tickers: list[str], 
        limit: str = "12"
    ) -> dict[str, "CashFlow | None"]:
        """
        Fetch cash flow statements for multiple tickers concurrently.
        Returns {ticker: CashFlow or None}.
        """
        async with httpx.AsyncClient() as session:
            tasks = [
                asyncio.create_task(self._cash_flow_single(session, sym, limit))
                for sym in tickers
            ]
            results = await asyncio.gather(*tasks)
        return dict(zip(tickers, results))

    async def income_statement_for_tickers(
        self, 
        tickers: list[str], 
        limit: str = "12"
    ) -> dict[str, "FinancialStatement | None"]:
        """
        Fetch income statements for multiple tickers concurrently.
        Returns {ticker: FinancialStatement or None}.
        """
        async with httpx.AsyncClient() as session:
            tasks = [
                asyncio.create_task(self._income_statement_single(session, sym, limit))
                for sym in tickers
            ]
            results = await asyncio.gather(*tasks)
        return dict(zip(tickers, results))

    async def order_flow_for_tickers(
        self, 
        tickers: list[str], 
        headers, 
        flow_type: str = "0", 
        count: str = "1"
    ) -> dict[str, "OrderFlow | None"]:
        """
        Fetch order flow data for multiple tickers concurrently.
        Returns {ticker: OrderFlow or None}.
        """
        async with httpx.AsyncClient(headers=headers) as session:
            tasks = [
                asyncio.create_task(self._order_flow_single(session, sym, headers, flow_type, count))
                for sym in tickers
            ]
            results = await asyncio.gather(*tasks)
        return dict(zip(tickers, results))

    async def capital_flow_for_tickers(
        self, 
        tickers: list[str]
    ) -> dict[str, tuple["CapitalFlow | None", "CapitalFlowHistory | None"]]:
        """
        Fetch capital flow data (latest + history) for multiple tickers concurrently.
        Returns {ticker: (CapitalFlow, CapitalFlowHistory) or (None, None)}.
        """
        async with httpx.AsyncClient() as session:
            tasks = [
                asyncio.create_task(self._capital_flow_single(session, sym))
                for sym in tickers
            ]
            results = await asyncio.gather(*tasks)
        return dict(zip(tickers, results))

    async def etf_holdings_for_tickers(
        self, 
        tickers: list[str], 
        pageSize: str = "200"
    ) -> dict[str, "ETFHoldings | None"]:
        """
        Fetch ETF holdings for multiple tickers concurrently.
        Returns {ticker: ETFHoldings or None}.
        """
        async with httpx.AsyncClient() as session:
            tasks = [
                asyncio.create_task(self._etf_holdings_single(session, sym, pageSize))
                for sym in tickers
            ]
            results = await asyncio.gather(*tasks)
        return dict(zip(tickers, results))
    


    async def fetch_latest_rsi(self, session: aiohttp.ClientSession, ticker: str, timespan:str='day') -> tuple[str, float | None]:
        """
        Fetch the latest RSI value for a single ticker.
        Returns a tuple of (ticker, latest_rsi_value).
        If something goes wrong or no data is found, returns (ticker, None).
        """
        params = {
            "timespan": timespan,
            "adjusted": "true",
            "window": "14",
            "series_type": "close",
            "order": "desc",
            "limit": "1",        # We only need the single most recent (latest) value
            "apiKey": self.api_key
        }
        url = f"https://api.polygon.io/v1/indicators/rsi/{ticker}"
        
        try:
            async with session.get(url, params=params) as response:
                response.raise_for_status()      # Raise an exception for 4xx/5xx errors
                data = await response.json()
                # Safely extract the RSI value if it exists
                results = data.get("results", {})
                values = results.get("values", [])
                if values:
                    # "order=desc" ensures the first item in `values` is the latest
                    return ticker, values[0]["value"]
                else:
                    return ticker, None
        except Exception:
            # Handle network/API errors
            return ticker, None

    async def fetch_rsi_for_tickers(self, tickers: list[str], timespan:str='day') -> dict[str, float | None]:
        """
        Fetch the latest RSI for multiple tickers concurrently.
        Returns a dict: { ticker: latest_rsi_value_or_None }.
        """
        async with aiohttp.ClientSession() as session:
            # Create a task for each ticker
            tasks = [
                asyncio.create_task(self.fetch_latest_rsi(session, ticker, timespan=timespan))
                for ticker in tickers
            ]
            # Run tasks concurrently
            results = await asyncio.gather(*tasks)
            # Convert list of tuples into a dictionary { ticker: rsi }
            return dict(results)


    def extract_rsi_value(self, rsi_data):
        """Helper method to extract the most recent RSI value safely."""
        try:
            if rsi_data and 'results' in rsi_data:
                values = rsi_data['results'].get('values')
                if values and len(values) > 0:
                    return values[-1]['value']  # Get the latest RSI value
        except Exception as e:
            print(f"Error extracting RSI value: {e}")
        return None
    async def rsi_snapshot(self, tickers: List[str]) -> pd.DataFrame:
        """
        Gather a snapshot of the RSI across multiple timespans for multiple tickers.
        """
        timespans = ['minute', 'day', 'hour', 'week', 'month']
        tasks = []
        for timespan in timespans:
            tasks.append(self.rsi(tickers, timespan))

        # Run RSI calculations concurrently for all timespans
        rsi_results = await asyncio.gather(*tasks, return_exceptions=True)

        # Aggregate the results
        aggregated_data = {}
        for timespan, rsi_data in zip(timespans, rsi_results):
            if isinstance(rsi_data, Exception):
                print(f"Error fetching RSI data for timespan '{timespan}': {rsi_data}")
                continue
            for ticker, data in rsi_data.items():
                if ticker not in aggregated_data:
                    aggregated_data[ticker] = {}
                rsi_value = self.extract_rsi_value(data)
                if rsi_value is not None:
                    aggregated_data[ticker][f"{timespan}_rsi"] = rsi_value

        # Convert aggregated data to DataFrame
        records = []
        for ticker, rsi_values in aggregated_data.items():
            record = {'ticker': ticker}
            record.update(rsi_values)
            if len(rsi_values) > 0:
                records.append(record)

        if records:
            df = pd.DataFrame(records)
            return df
        else:
            print("No RSI data available for the provided tickers.")
            return None



    
        


    async def fetch_macd(self, session: aiohttp.ClientSession, ticker: str, timespan:str='day') -> dict:
        """
        Fetches the last 3 MACD data points for the given ticker.
        Returns a dict like:
            {
              "ticker": str,
              "hist_values": [hist1, hist2, hist3, ...]  # newest first
            }
        """
        params = {
            "timespan": timespan,
            "adjusted": "true",
            "short_window": "12",
            "long_window": "26",
            "signal_window": "9",
            "series_type": "close",
            "order": "desc",   # newest data first
            "limit": "3",      # get 3 points so we can analyze
            "apiKey": self.api_key
        }
        url = f"https://api.polygon.io/v1/indicators/macd/{ticker}"
        
        try:
            async with session.get(url, params=params) as response:
                response.raise_for_status()
                data = await response.json()

                # Parse MACD values
                results = data.get("results", {})
                values = results.get("values", [])
                
                # We only need the histogram data
                hist_values = []
                for item in values:
                    # "histogram" is the MACD histogram for this period
                    h = item.get("histogram")
                    if h is not None:
                        hist_values.append(h)

                # 'hist_values' will be in reverse chronological order (newest first)
                return {"ticker": ticker, "hist_values": hist_values}
        
        except Exception:
            # Return empty list if any error
            return {"ticker": ticker, "hist_values": []}
        
    def check_macd_sentiment(self, hist: list) -> str:
        """
        Analyze the MACD histogram to determine if the sentiment is bullish or bearish.
        - Returns 'bullish' if the histogram shows a bullish setup.
        - Returns 'bearish' if the histogram shows a bearish setup.
        - Returns '-' if no clear signal is detected.
        
        Expecting 'hist' to be in reverse-chronological order (newest first).
        """
        try:
            # Ensure histogram has at least 3 values
            if not hist or len(hist) < 3:
                return '-'

            # Take the last three values (still newest first).
            last_three_values = hist[:3]

            # Check for bullish sentiment (close to -0.02 & trending "down" in hist)
            if (
                abs(last_three_values[0] + 0.02) < 0.04  # first item close to -0.02
                and all(last_three_values[i] > last_three_values[i + 1] for i in range(len(last_three_values) - 1))
            ):
                return 'bullish'

            # Check for bearish sentiment (close to +0.02 & trending "up" in hist)
            if (
                abs(last_three_values[0] - 0.02) < 0.04
                and all(last_three_values[i] < last_three_values[i + 1] for i in range(len(last_three_values) - 1))
            ):
                return 'bearish'

            # No clear signal
            return '-'

        except Exception as e:
            print(f"Error analyzing MACD sentiment: {e}")
            return '-'
        

    async def fetch_macd_signals_for_tickers(self, tickers: list[str], timespan:str='day') -> dict[str, str]:
        """
        1. Concurrently fetch MACD data (histogram) for each ticker (last 3 data points).
        2. Determine if there's a bullish or bearish sentiment, or no signal.
        3. Return a mapping of {ticker: "bullish"/"bearish"/"-"}.
        """
        async with aiohttp.ClientSession() as session:
            # Fetch data for all tickers in parallel
            tasks = [asyncio.create_task(self.fetch_macd(session, t, timespan=timespan)) for t in tickers]
            results = await asyncio.gather(*tasks)

        signals = {}
        for result in results:
            ticker = result["ticker"]
            # 'hist_values' is a list of floats for the histogram
            hist_values = result["hist_values"]

            # Analyze sentiment
            sentiment = self.check_macd_sentiment(hist_values)
            signals[ticker] = sentiment

        return signals
    


    async def get_option_chain_all(
        self,
        underlying_asset: str,
        strike_price: float = None,
        strike_price_lte: float = None,
        strike_price_gte: float = None,
        expiration_date: str = None,
        expiration_date_gte: str = None,
        expiration_date_lte: str = None,
        contract_type: str = None,
        order: str = None,
        limit: int = 250,
        sort: str = None,
        insert: bool = False
    ):
        """
        Retrieve all options contracts for a specific underlying asset (ticker symbol) across multiple pages.
        """
        try:
            if not underlying_asset:
                raise ValueError("Underlying asset ticker symbol must be provided.")

            # Handle special case for index assets (e.g., "I:SPX" for S&P 500 Index)
            if underlying_asset.startswith("I:"):
                underlying_asset = underlying_asset.replace("I:", "")

            # Build query parameters
            params = {
                'strike_price': strike_price,
                'strike_price.lte': strike_price_lte,
                'strike_price.gte': strike_price_gte,
                'expiration_date': expiration_date,
                'expiration_date.gte': expiration_date_gte,
                'expiration_date.lte': expiration_date_lte,
                'contract_type': contract_type,
                'order': order,
                'limit': limit,
                'sort': sort
            }

            # Filter out None values
            params = {key: value for key, value in params.items() if value is not None}

            # Construct the API endpoint and query string
            endpoint = f"https://api.polygon.io/v3/snapshot/options/{underlying_asset}"
            if params:
                query_string = '&'.join([f"{key}={value}" for key, value in params.items()])
                endpoint += '?' + query_string
            endpoint += f"&apiKey={self.api_key}"

            logging.debug(f"Fetching option chain data for {underlying_asset} with query: {params}")

            # Fetch the data using asynchronous pagination
            response_data = await self.paginate_concurrent(endpoint)

            # Parse response data into a structured option snapshot object
            option_data = UniversalOptionSnapshot(response_data)

            # Insert into the database if specified
            if insert:
                logging.info("Inserting option chain data into the database.")
                await self.connect()  # Ensure connection to the database
                await self.batch_insert_dataframe(
                    option_data.df,
                    table_name='all_options',
                    unique_columns='option_symbol'
                )

            logging.info("Option chain data retrieval successful.")
            return option_data

        except ValueError as ve:
            logging.error(f"ValueError occurred: {ve}")
            return None
        except Exception as e:
            logging.error(f"An error occurred while fetching the option chain: {e}")
            return None

    async def paginate_concurrent(self, url, as_dataframe=False, concurrency=25):
        """
        Concurrently paginates through polygon.io endpoints that contain the "next_url".
        """
        all_results = []
        pages_to_fetch = [url]

        while pages_to_fetch:
            tasks = []
            for _ in range(min(concurrency, len(pages_to_fetch))):
                next_url = pages_to_fetch.pop(0)
                tasks.append(self.fetch_page(next_url))

            results = await asyncio.gather(*tasks)
            if results is not None:
                for data in results:
                    if data is not None:
                        if "results" in data:
                            all_results.extend(data["results"])
                        next_url = data.get("next_url")
                        if next_url:
                            next_url += f'&{urlencode({"apiKey": f"{self.api_key}"})}'
                            pages_to_fetch.append(next_url)
                    else:
                        break

        if as_dataframe:
            return pd.DataFrame(all_results)
        else:
            return all_results

    async def fetch_page(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.json()

    # ------------------------------------------------
    #  NEW: Multi-ticker concurrency
    # ------------------------------------------------
    async def get_option_chain_for_tickers(
        self,
        tickers: list[str],
        strike_price: float = None,
        strike_price_lte: float = None,
        strike_price_gte: float = None,
        expiration_date: str = None,
        expiration_date_gte: str = None,
        expiration_date_lte: str = None,
        contract_type: str = None,
        order: str = None,
        limit: int = 250,
        sort: str = None,
        insert: bool = False
    ) -> dict[str, UniversalOptionSnapshot | None]:
        """
        Concurrently fetch option chain data for multiple tickers.

        Returns:
            A dict mapping each ticker to either:
              - A UniversalOptionSnapshot object (if successful),
              - or None (if an error occurred).
        """
        tasks = []
        for ticker in tickers:
            task = asyncio.create_task(
                self.get_option_chain_all(
                    underlying_asset=ticker,
                    strike_price=strike_price,
                    strike_price_lte=strike_price_lte,
                    strike_price_gte=strike_price_gte,
                    expiration_date=expiration_date,
                    expiration_date_gte=expiration_date_gte,
                    expiration_date_lte=expiration_date_lte,
                    contract_type=contract_type,
                    order=order,
                    limit=limit,
                    sort=sort,
                    insert=insert
                )
            )
            tasks.append(task)

        results = await asyncio.gather(*tasks, return_exceptions=True)

        out = {}
        for idx, ticker in enumerate(tickers):
            if isinstance(results[idx], Exception):
                logging.error(f"Error fetching {ticker}: {results[idx]}")
                out[ticker] = None
            else:
                out[ticker] = results[idx]

        return out