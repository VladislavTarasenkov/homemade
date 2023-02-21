import requests
from pybit import spot
from pybit import HTTP  # supports inverse perp & futures, usdt perp, spot.
from pybit.spot import HTTP
from pprint import pprint
from pybit import inverse_perpetual  # <-- import HTTP & WSS for inverse perp
from pybit import spot  # <-- import HTTP & WSS for spot
import time
session_unauth = inverse_perpetual.HTTP(endpoint="https://api.bybit.com")
from config import api_key, api_secret

# Authenticated
session_auth = inverse_perpetual.HTTP(
    endpoint="https://api.bybit.com",
    api_key=api_key,
    api_secret=api_secret
)
info = session_auth.latest_information_for_symbol(symbol="ETHUSDT")
print(info)

url = "https://api.bybit.com"

SYMBOL = "ETHUSDT"

def changes():
    change = session_auth.latest_information_for_symbol(symbol=SYMBOL)
    change = change["result"]

    for each in change:
        close = each["last_price"]
    return close
def main():
    print(SYMBOL)
    first_ord = changes()
    high = float(first_ord) * 1.01
    down = float(first_ord) * 0.99
    while True:
        if float(changes()) <= down or float(changes()) >= high:
            print(changes())
            high = float(changes()) * 1.01
            down = float(changes()) * 0.99
        time.sleep(1)
main()


