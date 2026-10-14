import pandas as pd


from fyers_apiv3 import fyersModel

APP_ID = "2Y07WWG8R9-200"
SECRET_KEY = "SFewn3gVxr8XvFgc"

session = fyersModel.SessionModel(
    client_id=APP_ID,
    secret_key=SECRET_KEY,
    grant_type="authorization_code"
)

access_token= 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiZDoxIiwiZDoyIiwieDowIiwieDoxIiwieDoyIl0sImF0X2hhc2giOiJnQUFBQUFCcXp2UWJDQUdTeGxMbjN0NkpFdk0wNElsR05oWXhvT0ppYnMwRDY3c1ZMSmhZTGFmTTRTWjBWOWN2bmYxMWMyOVE4UTFXOV9USnZPUU5tc3NlcElWU3d2TWRWUXNTWXUyVEx0M0c1X0h5VWVkZDlnOD0iLCJkaXNwbGF5X25hbWUiOiIiLCJvbXMiOiJLMSIsImhzbV9rZXkiOiI2ZjMwMmFhMGIwNjdiMDYzMmYyZjY3ZmY3ZTQ1NmE3MjQ4ZWZmODBhMmQ5YWU1YjY4OGQ4MGZlMyIsImlzRGRwaUVuYWJsZWQiOiJOIiwiaXNNdGZFbmFibGVkIjoiTiIsImZ5X2lkIjoiRkFCMzc5OTMiLCJhcHBUeXBlIjoyMDAsImV4cCI6MTc5MjAyNDIwMCwiaWF0IjoxNzkxOTQ3ODAzLCJpc3MiOiJhcGkuZnllcnMuaW4iLCJuYmYiOjE3OTE5NDc4MDMsInN1YiI6ImFjY2Vzc190b2tlbiJ9.pLiuHDO1OmOfL-qpfwRSmjvZvVJKmedOljDZrb2vViA'


app_id = "V02TYSP7SU-100"

fyers = fyersModel.FyersModel(
    client_id=app_id,
    token=access_token
)



from fyers_apiv3 import fyersModel
from datetime import datetime, timedelta

# Replace the following variables with your own values
symbol = "NSE:SBIN-EQ"
interval = "1D"
start_date = int((datetime.now() - timedelta(days=4)).timestamp())  # Convert start_date to epoch timestamp
to_date = int((datetime.now() - timedelta(days=1)).timestamp())  # Convert to_date to epoch timestamp

# Initialize the fyersModel instance
fyers = fyersModel.FyersModel(client_id=app_id, token=access_token)

data = {
    "symbol": symbol,
    "resolution": interval,
    "date_format": "0",
    "range_from": start_date,
    "range_to": to_date,
    "cont_flag": "1"
}

response = fyers.history(data)
print(response)


stocks = [
    "NSE:ADANIENSOL-EQ",
    "NSE:IDFCFIRSTB-EQ",
    "NSE:AMBUJACEM-EQ",
    "NSE:TECHM-EQ",
    "NSE:IDEA-EQ",
    "NSE:FORTIS-EQ",
    "NSE:DLF-EQ",
    "NSE:NMDC-EQ",
    "NSE:MANKIND-EQ",
    "NSE:HINDCOPPER-EQ",
    "NSE:LICHSGFIN-EQ",
    "NSE:M&M-EQ",
    "NSE:MARUTI-EQ",
    "NSE:PPLPHARMA-EQ",
    "NSE:ALKEM-EQ",
    "NSE:ABB-EQ",
    "NSE:HEROMOTOCO-EQ",
    "NSE:PHOENIXLTD-EQ",
    "NSE:POWERGRID-EQ",
    "NSE:JIOFIN-EQ",
    "NSE:KOTAKBANK-EQ",
    "NSE:BHARTIARTL-EQ",
    "NSE:UPL-EQ",
    "NSE:TCS-EQ",
    "NSE:ULTRACEMCO-EQ",
    "NSE:NTPC-EQ",
    "NSE:JSWSTEEL-EQ",
    "NSE:GRASIM-EQ",
    "NSE:KEI-EQ",
    "NSE:COLPAL-EQ",
    "NSE:IRB-EQ",
    "NSE:JSWENERGY-EQ",
    "NSE:ICICIPRULI-EQ",
    "NSE:VBL-EQ",
    "NSE:LAURUSLABS-EQ",
    "NSE:IRFC-EQ",
    "NSE:IREDA-EQ",
    "NSE:GODREJCP-EQ",
    "NSE:SYNGENE-EQ",
    "NSE:LUPIN-EQ",
    "NSE:PNB-EQ",
    "NSE:DIVISLAB-EQ",
    "NSE:INDIGO-EQ",
    "NSE:JSL-EQ",
    "NSE:IIFL-EQ",
    "NSE:GRANULES-EQ",
    "NSE:INFY-EQ",
    "NSE:UNIONBANK-EQ",
    "NSE:IGL-EQ",
    "NSE:LT-EQ",
    "NSE:COFORGE-EQ",
    "NSE:KAYNES-EQ",
    "NSE:LTIM-EQ",
    "NSE:GODREJPROP-EQ",
    "NSE:FEDERALBNK-EQ",
    "NSE:UNITDSPR-EQ",
    "NSE:OFSS-EQ",
    "NSE:POONAWALLA-EQ",
    "NSE:YESBANK-EQ",
    "NSE:IRCTC-EQ",
    "NSE:UNOMINDA-EQ",
    "NSE:PAGEIND-EQ",
    "NSE:TITAGARH-EQ",
    "NSE:RECLTD-EQ",
    "NSE:APOLLOHOSP-EQ",
    "NSE:BAJAJFINSV-EQ",
    "NSE:CROMPTON-EQ",
    "NSE:OIL-EQ",
    "NSE:SBICARD-EQ",
    "NSE:RBLBANK-EQ",
    "NSE:PERSISTENT-EQ",
    "NSE:PETRONET-EQ",
    "NSE:TRENT-EQ",
    "NSE:DMART-EQ",
    "NSE:PRESTIGE-EQ",
    "NSE:HDFCBANK-EQ",
    "NSE:HINDUNILVR-EQ",
    "NSE:HINDPETRO-EQ",
    "NSE:INDIANB-EQ",
    "NSE:ADANIPORTS-EQ",
    "NSE:INDHOTEL-EQ",
    "NSE:ITC-EQ",
    "NSE:MGL-EQ",
    "NSE:SJVN-EQ",
    "NSE:MANAPPURAM-EQ",
    "NSE:TATATECH-EQ",
    "NSE:INDUSTOWER-EQ",
    "NSE:VEDL-EQ",
    "NSE:SHREECEM-EQ",
    "NSE:MCX-EQ",
    "NSE:BAJFINANCE-EQ",
    "NSE:TORNTPHARM-EQ",
    "NSE:BHEL-EQ",
    "NSE:BANKINDIA-EQ",
    "NSE:MAZDOCK-EQ",
    "NSE:NYKAA-EQ",
    "NSE:JINDALSTEL-EQ",
    "NSE:TVSMOTOR-EQ",
    "NSE:ASHOKLEY-EQ",
    "NSE:BDL-EQ",
    "NSE:SBILIFE-EQ",
    "NSE:JUBLFOOD-EQ",
    "NSE:NESTLEIND-EQ",
    "NSE:HAL-EQ",
    "NSE:BSE-EQ",
    "NSE:OBEROIRLTY-EQ",
    "NSE:COALINDIA-EQ",
    "NSE:SOLARINDS-EQ",
    "NSE:GMRAIRPORT-EQ",
    "NSE:RELIANCE-EQ",
    "NSE:ASTRAL-EQ",
    "NSE:BALKRISIND-EQ",
    "NSE:BEL-EQ",
    "NSE:SHRIRAMFIN-EQ",
    "NSE:BAJAJ-AUTO-EQ",
    "NSE:SONACOMS-EQ",
    "NSE:INDUSINDBK-EQ",
    "NSE:CYIENT-EQ",
    "NSE:NHPC-EQ",
    "NSE:NATIONALUM-EQ",
    "NSE:CUMMINSIND-EQ",
    "NSE:BLUESTARCO-EQ",
    "NSE:ICICIGI-EQ",
    "NSE:ACC-EQ",
    "NSE:CANBK-EQ",
    "NSE:BIOCON-EQ",
    "NSE:M&MFIN-EQ",
    "NSE:HINDALCO-EQ",
    "NSE:TIINDIA-EQ",
    "NSE:NAUKRI-EQ",
    "NSE:TATAPOWER-EQ",
    "NSE:TORNTPOWER-EQ",
    "NSE:WIPRO-EQ",
    "NSE:HINDZINC-EQ",
    "NSE:PFC-EQ",
    "NSE:EXIDEIND-EQ",
    "NSE:CHOLAFIN-EQ",
    "NSE:BSOFT-EQ",
    "NSE:IOC-EQ",
    "NSE:MFSL-EQ",
    "NSE:PATANJALI-EQ",
    "NSE:HFCL-EQ",
    "NSE:PNBHOUSING-EQ",
    "NSE:HUDCO-EQ",
    "NSE:ABCAPITAL-EQ",
    "NSE:IEX-EQ",
    "NSE:BANDHANBNK-EQ",
    "NSE:ASIANPAINT-EQ",
    "NSE:MUTHOOTFIN-EQ",
    "NSE:SBIN-EQ",
    "NSE:PEL-EQ",
    "NSE:SUPREMEIND-EQ",
    "NSE:ADANIGREEN-EQ",
    "NSE:HDFCAMC-EQ",
    "NSE:BRITANNIA-EQ",
    "NSE:CHAMBLFERT-EQ",
    "NSE:POLICYBZR-EQ",
    "NSE:CIPLA-EQ",
    "NSE:GLENMARK-EQ",
    "NSE:CDSL-EQ",
    "NSE:DIXON-EQ",
    "NSE:TATACONSUM-EQ",
    "NSE:TITAN-EQ",
    "NSE:NCC-EQ",
    "NSE:HDFCLIFE-EQ",
    "NSE:APLAPOLLO-EQ",
    "NSE:AARTIIND-EQ",
    "NSE:HCLTECH-EQ",
    "NSE:LODHA-EQ",
    "NSE:CAMS-EQ",
    "NSE:CGPOWER-EQ",
    "NSE:INOXWIND-EQ",
    "NSE:BHARATFORG-EQ",
    "NSE:ZYDUSLIFE-EQ",
    "NSE:MPHASIS-EQ",
    "NSE:GAIL-EQ",
    "NSE:BPCL-EQ",
    "NSE:AXISBANK-EQ",
    "NSE:PAYTM-EQ",
    "NSE:BOSCHLTD-EQ",
    "NSE:PIIND-EQ",
    "NSE:ONGC-EQ",
    "NSE:LTF-EQ",
    "NSE:ADANIENT-EQ",
    "NSE:LICI-EQ",
    "NSE:KALYANKJIL-EQ",
    "NSE:SAIL-EQ",
    "NSE:SUNPHARMA-EQ",
    "NSE:TATASTEEL-EQ",
    "NSE:TATACOMM-EQ",
    "NSE:VOLTAS-EQ",
    "NSE:BANKBARODA-EQ",
    "NSE:CONCOR-EQ",
    "NSE:AUROPHARMA-EQ",
    "NSE:ABFRL-EQ",
    "NSE:SIEMENS-EQ",
    "NSE:TATACHEM-EQ",
    "NSE:TATAELXSI-EQ",
    "NSE:MOTHERSON-EQ",
    "NSE:RVNL-EQ",
    "NSE:DELHIVERY-EQ",
    "NSE:DABUR-EQ",
    "NSE:DALBHARAT-EQ",
    "NSE:AUBANK-EQ",
    "NSE:MAXHEALTH-EQ",
    "NSE:PIDILITIND-EQ",
    "NSE:NBCC-EQ",
    "NSE:ANGELONE-EQ",
    "NSE:SRF-EQ",
    "NSE:TATAMOTORS-EQ",
    "NSE:MARICO-EQ",
    "NSE:ETERNAL-EQ",
    "NSE:ICICIBANK-EQ",
    "NSE:ATGL-EQ",
    "NSE:CESC-EQ",
    "NSE:POLYCAB-EQ",
    "NSE:DRREDDY-EQ",
    "NSE:KPITTECH-EQ",
    "NSE:EICHERMOT-EQ",
    "NSE:HAVELLS-EQ"
]


LOT_SIZES = {
    "NSE:ADANIENSOL-EQ": 675,
    "NSE:IDFCFIRSTB-EQ": 9275,
    "NSE:AMBUJACEM-EQ": 1200,
    "NSE:TECHM-EQ": 600,
    "NSE:IDEA-EQ": 71475,
    "NSE:FORTIS-EQ": 775,
    "NSE:DLF-EQ": 950,
    "NSE:NMDC-EQ": 6750,
    "NSE:MANKIND-EQ": 250,

    "NSE:LICHSGFIN-EQ": 1000,
    "NSE:M&M-EQ": 200,
    "NSE:MARUTI-EQ": 50,    "NSE:ALKEM-EQ": 125,
    "NSE:ABB-EQ": 125,
    "NSE:HEROMOTOCO-EQ": 150,
    "NSE:PHOENIXLTD-EQ": 350,
    "NSE:POWERGRID-EQ": 1900,
    "NSE:JIOFIN-EQ": 2350,
    "NSE:KOTAKBANK-EQ": 2000,
    "NSE:BHARTIARTL-EQ": 475,
    "NSE:UPL-EQ": 1355,
    "NSE:TCS-EQ": 225,
    "NSE:ULTRACEMCO-EQ": 50,
    "NSE:NTPC-EQ": 1500,
    "NSE:JSWSTEEL-EQ": 675,
    "NSE:GRASIM-EQ": 250,
    "NSE:KEI-EQ": 175,
    "NSE:COLPAL-EQ": 275,
    "NSE:IRB-EQ": None,
    "NSE:JSWENERGY-EQ": 1075,
    "NSE:ICICIPRULI-EQ": 925,
    "NSE:VBL-EQ": 1275,
    "NSE:LAURUSLABS-EQ": 850,
    "NSE:IRFC-EQ": 5425,
    "NSE:IREDA-EQ": 4525,        # no Dec 2026 contract (leaving F&O)
    "NSE:GODREJCP-EQ": 500,
    "NSE:SYNGENE-EQ": None,
    "NSE:LUPIN-EQ": 425,
    "NSE:PNB-EQ": 8000,
    "NSE:DIVISLAB-EQ": 100,
    "NSE:INDIGO-EQ": 150,
    "NSE:JSL-EQ": None,
    "NSE:IIFL-EQ": None,
    "NSE:GRANULES-EQ": None,
    "NSE:INFY-EQ": 400,
    "NSE:UNIONBANK-EQ": 4425,
    "NSE:IGL-EQ": None,
    "NSE:LT-EQ": 175,
    "NSE:COFORGE-EQ": 475,
    "NSE:KAYNES-EQ": 150,
    "NSE:LTIM-EQ": 150,          # now listed as LTM
    "NSE:GODREJPROP-EQ": 325,
    "NSE:FEDERALBNK-EQ": 2500,
    "NSE:UNITDSPR-EQ": 400,
    "NSE:OFSS-EQ": 100,
    "NSE:POONAWALLA-EQ": None,
    "NSE:YESBANK-EQ": 31100,
    "NSE:IRCTC-EQ": None,
    "NSE:UNOMINDA-EQ": 550,
    "NSE:PAGEIND-EQ": 20,
    "NSE:TITAGARH-EQ": None,
    "NSE:RECLTD-EQ": 1575,
    "NSE:APOLLOHOSP-EQ": 125,
    "NSE:BAJAJFINSV-EQ": 300,
    "NSE:CROMPTON-EQ": 2150,
    "NSE:OIL-EQ": 1400,
    "NSE:SBICARD-EQ": 800,
    "NSE:RBLBANK-EQ": 3175,
    "NSE:PERSISTENT-EQ": 125,
    "NSE:PETRONET-EQ": 1900,
    "NSE:TRENT-EQ": 225,
    "NSE:DMART-EQ": 150,
    "NSE:PRESTIGE-EQ": 450,
    "NSE:HDFCBANK-EQ": 650,
    "NSE:HINDUNILVR-EQ": 300,
    "NSE:HINDPETRO-EQ": 2025,
    "NSE:INDIANB-EQ": 1000,
    "NSE:ADANIPORTS-EQ": 475,
    "NSE:INDHOTEL-EQ": 1000,
    "NSE:ITC-EQ": 1725,
    "NSE:MGL-EQ": None,
    "NSE:SJVN-EQ": None,
    "NSE:MANAPPURAM-EQ": 3000,
    "NSE:TATATECH-EQ": None,
    "NSE:INDUSTOWER-EQ": 1700,
    "NSE:VEDL-EQ": 1150,
    "NSE:SHREECEM-EQ": 25,
    "NSE:MCX-EQ": 225,
    "NSE:BAJFINANCE-EQ": 750,
    "NSE:TORNTPHARM-EQ": 125,
    "NSE:BHEL-EQ": 2625,
    "NSE:BANKINDIA-EQ": 5200,
    "NSE:MAZDOCK-EQ": 225,
    "NSE:NYKAA-EQ": 3125,
    "NSE:JINDALSTEL-EQ": 625,
    "NSE:TVSMOTOR-EQ": 175,
    "NSE:ASHOKLEY-EQ": 5000,
    "NSE:BDL-EQ": 425,
    "NSE:SBILIFE-EQ": 375,
    "NSE:JUBLFOOD-EQ": 1250,
    "NSE:NESTLEIND-EQ": 500,
    "NSE:HAL-EQ": 150,
    "NSE:BSE-EQ": 200,
    "NSE:OBEROIRLTY-EQ": 350,
    "NSE:COALINDIA-EQ": 1350,
    "NSE:SOLARINDS-EQ": 50,
    "NSE:GMRAIRPORT-EQ": 6975,
    "NSE:RELIANCE-EQ": 500,
    "NSE:ASTRAL-EQ": 425,
    "NSE:BALKRISIND-EQ": None,
    "NSE:BEL-EQ": 1425,
    "NSE:SHRIRAMFIN-EQ": 825,
    "NSE:BAJAJ-AUTO-EQ": 75,
    "NSE:SONACOMS-EQ": 1225,
    "NSE:INDUSINDBK-EQ": 700,
    "NSE:CYIENT-EQ": None,
    "NSE:NHPC-EQ": 6950,
    "NSE:NATIONALUM-EQ": 1875,
    "NSE:CUMMINSIND-EQ": 200,
    "NSE:BLUESTARCO-EQ": 325,
    "NSE:ICICIGI-EQ": 325,
    "NSE:ACC-EQ": None,
    "NSE:CANBK-EQ": 6750,
    "NSE:BIOCON-EQ": 2500,
    "NSE:M&MFIN-EQ": None,
    "NSE:HINDALCO-EQ": 700,
    "NSE:TIINDIA-EQ": 200,
    "NSE:NAUKRI-EQ": 550,
    "NSE:TATAPOWER-EQ": 1450,
    "NSE:TORNTPOWER-EQ": None,
    "NSE:WIPRO-EQ": 3000,
    "NSE:HINDZINC-EQ": 1225,
    "NSE:PFC-EQ": 1300,
    "NSE:EXIDEIND-EQ": None,
    "NSE:CHOLAFIN-EQ": 625,
    "NSE:BSOFT-EQ": None,
    "NSE:IOC-EQ": 4875,
    "NSE:MFSL-EQ": 400,
    "NSE:PATANJALI-EQ": 1075,
    "NSE:HFCL-EQ": None,
    "NSE:PNBHOUSING-EQ": 650,
    "NSE:HUDCO-EQ": None,
    "NSE:ABCAPITAL-EQ": 3100,
    "NSE:IEX-EQ": 4350,          # no Dec 2026 contract (leaving F&O)
    "NSE:BANDHANBNK-EQ": 3600,
    "NSE:ASIANPAINT-EQ": 250,
    "NSE:MUTHOOTFIN-EQ": 275,
    "NSE:SBIN-EQ": 750,
    "NSE:PEL-EQ": None,
    "NSE:SUPREMEIND-EQ": 175,
    "NSE:ADANIGREEN-EQ": 600,
    "NSE:HDFCAMC-EQ": 300,
    "NSE:BRITANNIA-EQ": 125,
    "NSE:CHAMBLFERT-EQ": None,
    "NSE:POLICYBZR-EQ": 350,
    "NSE:CIPLA-EQ": 425,
    "NSE:GLENMARK-EQ": 375,
    "NSE:CDSL-EQ": 475,
    "NSE:DIXON-EQ": 50,
    "NSE:TATACONSUM-EQ": 550,
    "NSE:TITAN-EQ": 175,
    "NSE:NCC-EQ": None,
    "NSE:HDFCLIFE-EQ": 1100,
    "NSE:APLAPOLLO-EQ": 350,
    "NSE:AARTIIND-EQ": None,
    "NSE:HCLTECH-EQ": 400,
    "NSE:LODHA-EQ": 625,
    "NSE:CAMS-EQ": 825,
    "NSE:CGPOWER-EQ": 850,
    "NSE:INOXWIND-EQ": 6400,
    "NSE:BHARATFORG-EQ": 500,
    "NSE:ZYDUSLIFE-EQ": 900,
    "NSE:MPHASIS-EQ": 275,
    "NSE:GAIL-EQ": 3550,
    "NSE:BPCL-EQ": 1975,
    "NSE:AXISBANK-EQ": 625,
    "NSE:PAYTM-EQ": 725,
    "NSE:BOSCHLTD-EQ": 25,
    "NSE:PIIND-EQ": 175,
    "NSE:ONGC-EQ": 2250,
    "NSE:LTF-EQ": 2250,
    "NSE:ADANIENT-EQ": 309,
    "NSE:LICI-EQ": 1400,
    "NSE:KALYANKJIL-EQ": 1350,
    "NSE:SAIL-EQ": 4700,
    "NSE:SUNPHARMA-EQ": 350,
    "NSE:TATASTEEL-EQ": 2750,
    "NSE:TATACOMM-EQ": None,
    "NSE:VOLTAS-EQ": 375,
    "NSE:BANKBARODA-EQ": 2925,
    "NSE:CONCOR-EQ": 1250,
    "NSE:AUROPHARMA-EQ": 550,
    "NSE:ABFRL-EQ": None,
    "NSE:SIEMENS-EQ": 175,
    "NSE:TATACHEM-EQ": None,
    "NSE:TATAELXSI-EQ": 125,
    "NSE:MOTHERSON-EQ": 6150,
    "NSE:RVNL-EQ": 1925,
    "NSE:DELHIVERY-EQ": 2075,
    "NSE:DABUR-EQ": 1250,
    "NSE:DALBHARAT-EQ": None,
    "NSE:AUBANK-EQ": 1000,
    "NSE:MAXHEALTH-EQ": 525,
    "NSE:PIDILITIND-EQ": 500,
    "NSE:NBCC-EQ": 6500,
    "NSE:ANGELONE-EQ": 2500,
    "NSE:SRF-EQ": 200,
    "NSE:TATAMOTORS-EQ": 1600,   # now TMPV (passenger vehicles) after demerger
    "NSE:MARICO-EQ": 1200,
    "NSE:ETERNAL-EQ": 2425,
    "NSE:ICICIBANK-EQ": 700,
    "NSE:ATGL-EQ": None,
    "NSE:CESC-EQ": None,
    "NSE:POLYCAB-EQ": 125,
    "NSE:DRREDDY-EQ": 625,
    "NSE:KPITTECH-EQ": 775,
    "NSE:EICHERMOT-EQ": 100,
    "NSE:HAVELLS-EQ": 500,
}
 



def format_candles(response):
    df = pd.DataFrame(
        response["candles"],
        columns=["timestamp", "open", "high", "low", "close", "volume"]
    )

    df["Datetime"] = (
        pd.to_datetime(df["timestamp"], unit="s", utc=True)
        .dt.tz_convert("Asia/Kolkata")
        .dt.strftime("%d-%m-%Y %H:%M")
    )

    # Typical Price
    typical_price = (df["high"] + df["low"] + df["close"]) / 3

    # Cumulative VWAP
    df["vwap"] = (
        (typical_price * df["volume"]).cumsum()
        / df["volume"].cumsum()
    )

    return df[
        ["Datetime", "open", "high", "low", "close", "volume", "vwap"]
    ]



def fyers_option_chain_df(response):
    # Check API status at the outer level
    if response.get("s") != "ok":
        raise ValueError(
            f"API error: {response.get('message', 'Unknown error')}"
        )

    # Extract the actual payload
    data = response["data"]
    options = data.get("optionsChain", [])

    rows = {}

    for opt in options:
        strike = opt.get("strike_price")
        opt_type = opt.get("option_type")

        # Skip underlying instrument (e.g. TCS-EQ)
        if opt_type not in ("CE", "PE") or strike in (None, -1):
            continue

        row = rows.setdefault(
            strike, {"strike_price": strike}
        )

        prefix = f"{opt_type}_"

        for key, value in opt.items():
            if key in ("strike_price", "option_type"):
                continue

            if key == "greeks" and isinstance(value, dict):
                for greek, greek_value in value.items():
                    row[f"{prefix}{greek}"] = greek_value
            elif key != "greeks":
                row[f"{prefix}{key}"] = value

    df = pd.DataFrame(list(rows.values()))

    if not df.empty:
        df = df.sort_values("strike_price").reset_index(drop=True)

    return df




import pandas as pd
import re


def _local_timestamp(value):
    """Convert a timestamp to timezone-naive India local time."""
    ts = pd.Timestamp(value)

    if ts.tzinfo is not None:
        ts = ts.tz_convert("Asia/Kolkata").tz_localize(None)

    return ts



import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo


# ============================================================
# CONFIGURATION
# ============================================================


# IMPORTANT: Configure the actual current lot size for each stock.
# Do not use a different stock's lot size.


RESOLUTION = "5"
CANDLE_INTERVAL = "5min"
DATE_FORMAT = "1"
CONT_FLAG = "1"

STRIKECOUNT = 5
USE_GREEKS = "1"

MIN_LOTS = 375
OI_RATIO = 3
ITM_COUNT = 5
OTM_COUNT = 5

TIMESTAMP_LABEL = "start"


# ============================================================
# HELPERS
# ============================================================

def normalize_symbol(exchange_symbol):
    """Convert NSE:ADANIENSOL-EQ to ADANIENSOL."""
    return exchange_symbol.split(":")[-1].removesuffix("-EQ")


def get_trading_date():
    """Use the current date in Indian market time."""
    return datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%Y-%m-%d")


def scan_one_stock(
    stock_data,
    option_chain_df,
    symbol,
    lot_size,
    current_time="now",
    min_lots=300,
    oi_ratio=3.0,
    itm_count=5,
    otm_count=5,
    candle_interval="5min",
    timestamp_label="start",):
    """
    Return a result dictionary if the stock passes all filters,
    otherwise return None.

    stock_data:
        Datetime, open, high, low, close, volume, vwap

    option_chain_df:
        strike_price, CE_oich, PE_oich, and related option columns

    timestamp_label:
        'start': Datetime represents candle start time.
        'end':   Datetime represents candle close time.

    current_time:
        'now', '10:00:00', or a full datetime string.
    """

    # --------------------------------------------------
    # 1. Validate inputs
    # --------------------------------------------------
    if lot_size <= 0:
        raise ValueError("lot_size must be greater than zero.")

    if min_lots < 0 or oi_ratio < 1:
        raise ValueError("min_lots must be >= 0 and oi_ratio >= 1.")

    if timestamp_label not in ("start", "end"):
        raise ValueError("timestamp_label must be 'start' or 'end'.")

    stock_required = {"Datetime", "close", "vwap"}
    option_required = {"strike_price", "CE_oich", "PE_oich"}

    if not stock_required.issubset(stock_data.columns):
        raise ValueError(
            f"stock_data must contain {stock_required}"
        )

    if not option_required.issubset(option_chain_df.columns):
        raise ValueError(
            f"option_chain_df must contain {option_required}"
        )

    # --------------------------------------------------
    # 2. Parse stock timestamps
    # --------------------------------------------------
    candles = stock_data.copy()

    candles["Datetime"] = pd.to_datetime(
        candles["Datetime"], 
        format="%d-%m-%Y %H:%M",
        errors="coerce"
    )

    if isinstance(candles["Datetime"].dtype, pd.DatetimeTZDtype):
        candles["Datetime"] = (
            candles["Datetime"]
            .dt.tz_convert("Asia/Kolkata")
            .dt.tz_localize(None)
        )

    candles["close"] = pd.to_numeric(
        candles["close"], errors="coerce"
    )
    candles["vwap"] = pd.to_numeric(
        candles["vwap"], errors="coerce"
    )

    candles = candles.dropna(
        subset=["Datetime", "close", "vwap"]
    ).sort_values("Datetime")

    if candles.empty:
        return None

    # --------------------------------------------------
    # 3. Resolve current_time
    # --------------------------------------------------
    time_only = (
        isinstance(current_time, str)
        and re.fullmatch(
            r"\d{1,2}:\d{2}(:\d{2})?", current_time.strip()
        )
    )

    if current_time is None or (
        isinstance(current_time, str)
        and current_time.strip().lower() == "now"
    ):
        cutoff = pd.Timestamp.now(tz="Asia/Kolkata")
        cutoff = cutoff.tz_localize(None)

    elif time_only:
        # Useful for testing historical intraday data.
        session_date = candles["Datetime"].max().normalize()
        parsed_time = pd.to_datetime(
            current_time.strip(), format=(
                "%H:%M:%S" if current_time.count(":") == 2
                else "%H:%M"
            )
        ).time()

        cutoff = pd.Timestamp.combine(
            session_date.date(), parsed_time
        )

    else:
        cutoff = _local_timestamp(current_time)

    # Only candles from the requested trading date
    session = candles[
        candles["Datetime"].dt.normalize() == cutoff.normalize()
    ].copy()

    if session.empty:
        return None

    # --------------------------------------------------
    # 4. Keep completed candles only
    # --------------------------------------------------
    if timestamp_label == "start":
        completed_at = (
            session["Datetime"] + pd.Timedelta(candle_interval)
        )
        session = session[completed_at <= cutoff]
    else:
        session = session[session["Datetime"] <= cutoff]

    if session.empty:
        return None

    latest = session.iloc[-1]
    close = float(latest["close"])
    vwap = float(latest["vwap"])

    # --------------------------------------------------
    # 5. Latest completed candle VWAP filter
    # --------------------------------------------------
    if close > vwap:
        price_direction = "BULLISH"
    elif close < vwap:
        price_direction = "BEARISH"
    else:
        return None

    # --------------------------------------------------
    # 6. Select ATM + ITM + OTM strikes
    # --------------------------------------------------
    chain = option_chain_df.copy()

    chain["strike_price"] = pd.to_numeric(
        chain["strike_price"], errors="coerce"
    )

    chain = (
        chain.dropna(subset=["strike_price"])
        .drop_duplicates("strike_price")
        .sort_values("strike_price")
        .reset_index(drop=True)
    )

    strikes = chain["strike_price"].tolist()

    if len(strikes) < itm_count + otm_count + 1:
        return None

    # Closest available strike to underlying close
    atm_idx = min(
        range(len(strikes)),
        key=lambda i: abs(strikes[i] - close)
    )

    start_idx = atm_idx - itm_count
    end_idx = atm_idx + otm_count + 1

    # Require the requested number on BOTH sides of ATM
    if start_idx < 0 or end_idx > len(strikes):
        return None

    selected = chain.iloc[start_idx:end_idx].copy()

    # --------------------------------------------------
    # 7. Aggregate net OI change over selected strikes
    # --------------------------------------------------
    selected["CE_oich"] = pd.to_numeric(
        selected["CE_oich"], errors="coerce"
    )
    selected["PE_oich"] = pd.to_numeric(
        selected["PE_oich"], errors="coerce"
    )

    # Missing contract-side OI changes are treated as zero.
    ce_net = selected["CE_oich"].fillna(0).sum()
    pe_net = selected["PE_oich"].fillna(0).sum()

    ce_abs = abs(ce_net)
    pe_abs = abs(pe_net)

    if ce_abs == pe_abs:
        return None

    if ce_abs > pe_abs:
        dominant_side = "CE"
        dominant_net = ce_net
        dominant_abs = ce_abs
        opposite_abs = pe_abs
    else:
        dominant_side = "PE"
        dominant_net = pe_net
        dominant_abs = pe_abs
        opposite_abs = ce_abs

    # --------------------------------------------------
    # 8. Absolute-magnitude dominance ratio
    # --------------------------------------------------
    if opposite_abs == 0:
        ratio = float("inf") if dominant_abs > 0 else 0.0
    else:
        ratio = dominant_abs / opposite_abs

    if ratio < oi_ratio:
        return None

    # --------------------------------------------------
    # 9. Minimum lots on dominant side only
    # --------------------------------------------------
    min_oi_quantity = min_lots * lot_size

    if dominant_abs < min_oi_quantity:
        return None

    # --------------------------------------------------
    # 10. Return only qualifying signals
    # --------------------------------------------------
    return {
        "timestamp": latest["Datetime"],
        "symbol": symbol,
        "close": close,
        "vwap": vwap,
        "price_direction": price_direction,
        "atm_strike": strikes[atm_idx],
        "selected_strikes": strikes[start_idx:end_idx],
        "strike_count": len(selected),
        "CE_net_oich": ce_net,
        "PE_net_oich": pe_net,
        "dominant_side": dominant_side,
        "dominant_net_oich": dominant_net,
        "oi_ratio": ratio,
        "dominant_change_lots": dominant_abs / lot_size,
        "min_lots": min_lots,
        "min_oi_quantity": min_oi_quantity,
    }


# ============================================================
# SCAN ALL STOCKS
# ============================================================

def scan_all_stocks(stocks, lot_sizes):
    """
    Fetch candles and option-chain data for every stock,
    run the existing scanner, and aggregate qualifying signals.

    Returns:
        all_signals_df
        bullish_df
        bearish_df
        Buying
        Selling
        errors_df
    """

    signals = []
    errors = []

    trading_date = get_trading_date()

    for exchange_symbol in stocks:

        symbol = normalize_symbol(exchange_symbol)

        try:
            # Fail safely if the stock's lot size is not configured.
            lot_size = lot_sizes.get(exchange_symbol)

            if lot_size is None or lot_size <= 0:
                raise ValueError(
                    f"Missing or invalid lot size for {exchange_symbol}"
                )

            # ------------------------------------------------
            # 1. FETCH OHLCV DATA
            # ------------------------------------------------

            ohlc_data = {
                "symbol": exchange_symbol,
                "resolution": RESOLUTION,
                "date_format": DATE_FORMAT,
                "range_from": trading_date,
                "range_to": trading_date,
                "cont_flag": CONT_FLAG,
            }

            data_response = fyers.history(data=ohlc_data)

            stock_data = format_candles(data_response)

            if stock_data is None or stock_data.empty:
                errors.append({
                    "symbol": symbol,
                    "stage": "OHLCV",
                    "error": "No candle data returned",
                })
                continue

            # ------------------------------------------------
            # 2. FETCH OPTION-CHAIN / OI DATA
            # ------------------------------------------------

            oi_data = {
                "symbol": exchange_symbol,
                "strikecount": STRIKECOUNT,
                "timestamp": "",
                "greeks": USE_GREEKS,
            }

            # Fyers API v3 Python SDK method
            oi_response = fyers.optionchain(data=oi_data)

            option_chain_df = fyers_option_chain_df(oi_response)

            if (
                option_chain_df is None
                or option_chain_df.empty
            ):
                errors.append({
                    "symbol": symbol,
                    "stage": "OPTION_CHAIN",
                    "error": "No option-chain data returned",
                })
                continue

            # ------------------------------------------------
            # 3. RUN YOUR EXISTING SIGNAL SCANNER
            # ------------------------------------------------

            result = scan_one_stock(
                stock_data=stock_data,
                option_chain_df=option_chain_df,
                symbol=symbol,
                lot_size=lot_size,
                current_time="now",
                min_lots=MIN_LOTS,
                oi_ratio=OI_RATIO,
                itm_count=ITM_COUNT,
                otm_count=OTM_COUNT,
                candle_interval=CANDLE_INTERVAL,
                timestamp_label=TIMESTAMP_LABEL,
            )

            # No qualifying signal is a normal outcome.
            if result is None:
                continue

            # Store each qualifying stock's result.
            signals.append(result)

        except Exception as exc:
            # One stock failing must not stop the entire scan.
            errors.append({
                "symbol": symbol,
                "stage": "SCAN",
                "error": str(exc),
            })

    # ========================================================
    # 4. BUILD MASTER DATAFRAME
    # ========================================================

    all_signals_df = pd.DataFrame(signals)

    # Ensure downstream filters work even when no stocks qualify.
    if all_signals_df.empty:
        all_signals_df = pd.DataFrame(
            columns=[
                "timestamp",
                "symbol",
                "close",
                "vwap",
                "price_direction",
                "oi_ratio",
            ]
        )

    # Remove any duplicate signal rows if the scanner returns them.
    if not all_signals_df.empty:
        all_signals_df = all_signals_df.drop_duplicates(
            subset=["symbol"],
            keep="last",
        ).reset_index(drop=True)

    # ========================================================
    # 5. SPLIT BULLISH AND BEARISH SIGNALS
    # ========================================================

    if not all_signals_df.empty:
        directions = (
            all_signals_df["price_direction"]
            .astype(str)
            .str.strip()
            .str.upper()
        )

        bullish_df = (
            all_signals_df.loc[directions == "BULLISH"]
            .reset_index(drop=True)
        )

        bearish_df = (
            all_signals_df.loc[directions == "BEARISH"]
            .reset_index(drop=True)
        )
    else:
        bullish_df = all_signals_df.copy()
        bearish_df = all_signals_df.copy()

    # ========================================================
    # 6. CREATE BUYING AND SELLING DICTIONARIES
    # ========================================================

    output_columns = [
        "symbol",
        "price_direction",
        "oi_ratio",
    ]

    def make_signal_dictionary(df):
        """Map each symbol to its selected signal fields."""

        if df.empty:
            return {}

        available_columns = [
            col for col in output_columns if col in df.columns
        ]

        return (
            df[available_columns]
            .drop_duplicates(subset=["symbol"], keep="last")
            .set_index("symbol")
            .to_dict(orient="index")
        )

    Buying = make_signal_dictionary(bullish_df)
    Selling = make_signal_dictionary(bearish_df)

    errors_df = pd.DataFrame(
        errors,
        columns=["symbol", "stage", "error"],
    )

    return (
        all_signals_df,
        bullish_df,
        bearish_df,
        Buying,
        Selling,
        errors_df,
    )


import streamlit as st
import pandas as pd

# ---- CHANGE THIS: import your own scanner + inputs ----
# from my_scanner import scan_all_stocks, stocks, LOT_SIZES
# -------------------------------------------------------

st.set_page_config(page_title="OI Ratio Ranking", layout="wide")
st.title("OI Ratio Ranking")

SHOW_COLS = [
    "rank", "symbol", "close", "vwap",
    "dominant_side", "dominant_net_oich", "oi_ratio", "dominant_change_lots",
]


@st.cache_data(ttl=60, show_spinner="Scanning stocks...")
def run_scan():
    all_signals_df, bullish_df, bearish_df, buying, selling, errors_df = scan_all_stocks(
        stocks=stocks,
        lot_sizes=LOT_SIZES,
    )
    return all_signals_df, errors_df


def build_rank(df: pd.DataFrame, direction: str) -> pd.DataFrame:
    out = (
        df[df["price_direction"] == direction]
        .drop_duplicates(subset="symbol")
        .sort_values("oi_ratio", ascending=False)
        .reset_index(drop=True)
    )
    out.insert(0, "rank", out.index + 1)
    return out[SHOW_COLS]


def show_table(title: str, df: pd.DataFrame):
    st.subheader(f"{title} ({len(df)})")
    if df.empty:
        st.info("No stocks.")
        return
    st.dataframe(
        df,
        hide_index=True,
        use_container_width=True,
        column_config={
            "oi_ratio": st.column_config.NumberColumn("OI Ratio", format="%.2f"),
            "close": st.column_config.NumberColumn(format="%.2f"),
            "vwap": st.column_config.NumberColumn(format="%.2f"),
            "dominant_net_oich": st.column_config.NumberColumn("Dominant Net OI Chg", format="%d"),
            "dominant_change_lots": st.column_config.NumberColumn("Change (lots)", format="%.0f"),
        },
    )


# ---- Controls ----
if st.button("🔄 Refresh"):
    run_scan.clear()

all_signals_df, errors_df = run_scan()

if all_signals_df.empty:
    st.warning("No qualifying signals right now.")
    st.stop()

st.caption(f"Last scan: {all_signals_df['timestamp'].max()}")

bull = build_rank(all_signals_df, "BULLISH")
bear = build_rank(all_signals_df, "BEARISH")

col1, col2 = st.columns(2)
with col1:
    show_table("🟢 Bullish", bull)
with col2:
    show_table("🔴 Bearish", bear)

if errors_df is not None and not errors_df.empty:
    with st.expander(f"Scan errors ({len(errors_df)})"):
        st.dataframe(errors_df, hide_index=True, use_container_width=True)









