import eel
import re
from main import Trading_bot

eel.init('web')

@eel.expose
def run_trade_bot(api_key, api_secret_key, amount):
    amount = int(amount) if amount.isdigit() else 500000
    run=Trading_bot(api_key, api_secret_key, amount=amount)
    run()

eel.start('main.html', size=(1200, 800))
