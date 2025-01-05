import pandas as pd
import logging
from data_market_index_fetcher.indexes.ibov.IbovWebScrapperB3 import IBovWebScrapperB3, Periodicity

# Suppress logs from IBovWebScrapperB3
logging.getLogger("IBovWebScrapper").setLevel(logging.ERROR)
logging.getLogger("LoggerUtil").setLevel(logging.ERROR)
logging.getLogger("WebDriverUtil").setLevel(logging.ERROR)
logging.getLogger("SeleniumUtil").setLevel(logging.ERROR)

ibov_scrapper=IBovWebScrapperB3()

periodicity_mapping = {
    Periodicity.DAILY: "D",
    Periodicity.WEEKLY: "W",
    Periodicity.MONTHLY: "ME",
    Periodicity.QUARTERLY: "Q",
    Periodicity.SEMESTRAL: "2Q",
    Periodicity.ANNUAL: "YE"
}


# Loop through each periodicity and fetch data
# Loop through each periodicity and fetch data
for periodicity, period_code in periodicity_mapping.items():
    # periodicity is a Periodicity enum, e.g., Periodicity.DAILY
    print(f"\nFetching data with {periodicity.value} periodicity.")
    
    # Pass the enum to fetch_data
    ibov_data = ibov_scrapper.fetch_data('2020-10-01', '2025-10-01', periodicity)
    
    print(f"{periodicity.value.capitalize()} Data:")
    print(ibov_data)

