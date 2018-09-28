import ssl
import pandas as pd


def get_appl_quote():
    """
    Get appl quote from the url, the value will be the higher value
    :return: String
    """
    ssl._create_default_https_context = ssl._create_unverified_context
    csv = pd.read_csv("https://stooq.com/q/l/?s=aapl.us&f=sd2t2ohlcv&h&e=csv")

    try:
        return "APPL quote is ${} per share.".format(csv.values[0][3])
    except Exception as e:
        return "APPL can't be found in this moment"
