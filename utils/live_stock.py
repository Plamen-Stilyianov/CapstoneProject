from typing import Any
from alpaca.data.live import StockDataStream

from decouple import config

api_key = config("ALPACA_KEY")
secret_key = config("ALPACA_SECRET")
live_data_url = config("ALPACA_WSS_URL")


wss_client = StockDataStream(api_key=api_key, secret_key=secret_key) #, url_override=live_data_url)

# async handler
async def quote_data_handler(data: Any):
    # quote data will arrive here
    print(data)
    # symbol='JPM' timestamp=datetime.datetime(2025, 7, 8, 13, 47, tzinfo=datetime.timezone.utc) open=286.49 high=286.81 low=286.49 close=286.81 volume=1002.0 trade_count=38.0 vwap=286.66
    # symbol='JPM' timestamp=datetime.datetime(2025, 7, 8, 13, 48, tzinfo=datetime.timezone.utc) open=287.04 high=287.26 low=287.04 close=287.1 volume=785.0 trade_count=17.0 vwap=287.143333

wss_client.subscribe_bars(quote_data_handler, "JPM")

wss_client.run()

# symbol='JPM' timestamp=datetime.datetime(2025, 7, 8, 13, 47, tzinfo=datetime.timezone.utc)
# open=286.49
# high=286.81
# low=286.49
# close=286.81
# volume=1002.0
# trade_count=38.0
# vwap=286.66