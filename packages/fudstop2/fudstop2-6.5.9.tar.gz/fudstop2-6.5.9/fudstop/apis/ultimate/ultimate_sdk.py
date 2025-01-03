import pandas as pd

from datetime import datetime, timedelta, timezone
import pytz
import aiohttp
import asyncio
import httpx

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

class UltimateSDK:
    def __init__(self):
    # ---------------------------------------------------------------
    # SINGLE-TICKER METHODS (as you already have them)
    # ---------------------------------------------------------------



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