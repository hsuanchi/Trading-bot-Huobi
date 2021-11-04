import eel
import re
from main import Trading_bot

eel.init('web')

@eel.expose
def run_trade_bot(api_key, api_secret_key, amount, price):
    amount = int(amount) if amount.isdigit() else 500000
    price = float(price) if re.match(r'^-?\d+(?:\.\d+)$', price) is not None else 0.0001
    run=Trading_bot(api_key, api_secret_key, amount=amount, price=price)
    run()

eel.start('main.html', size=(1200, 800))
