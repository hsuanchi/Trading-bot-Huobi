import eel
import re
from main import Trading_bot

eel.init('web')

@eel.expose
def run_trade_bot(account_id, api_key, api_secret_key, ammount, price):
    ammount = int(amount) if amount.isdigit() else 100000
    price = float(price) if re.match(r'^-?\d+(?:\.\d+)$', price) is None else 0.0001
    run=Trading_bot(account_id, api_key, api_secret_key, ammount, price)
    run()

eel.start('main.html', size=(1200, 800))
