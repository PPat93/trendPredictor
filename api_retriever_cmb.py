"""
API data retriever comb:
Sends data to Integrator -> Analyzer;
Sends API request to retrieve needed values;
Receives response with retrieved values;
Extract values from the response and deletes everything that is not needed;
"""

import os
import requests

API_KEY = os.environ.get("predictorRetrieverApiKey")

API_URI = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={API_KEY}&outputsize=compact"

res = requests.get(API_URI, timeout=10)

print(f"Status: {res.status_code}, Res: {res.content}")
