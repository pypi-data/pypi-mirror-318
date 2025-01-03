import pandas as pd
# from IbovWebScrapperB3 import IBovWebScrapperB3
from data_market_index_fetcher.indexes.ibov.IbovWebScrapperB3 import IBovWebScrapperB3


ibov_scrapper=IBovWebScrapperB3()

ibov_data=ibov_scrapper.fetch_data('2024-10-01', '2025-10-01')

print(ibov_data.tail())