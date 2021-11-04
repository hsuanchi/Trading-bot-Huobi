import time
from huobi.client.account import AccountClient
from huobi.client.trade import TradeClient
from huobi.constant import *
from huobi.utils import *


class Trading_bot:
    def __init__(self):
        # input your acount_id, access_key, secret_key below:
        self.g_api_key = "your api key"
        self.g_secret_key = "your api secret key"
        self.target_coin = "imxusdt"

    def __call__(self):
        account_client = AccountClient(
            api_key=self.g_api_key, secret_key=self.g_secret_key
        )

        LogInfo.output("====== Show Accounts ======")
        account_balance_list = account_client.get_account_balance()
        if account_balance_list and len(account_balance_list):
            for account_balance_obj in account_balance_list:
                if account_balance_obj and len(account_balance_obj.list):
                    PrintBasic.print_basic(account_balance_obj.id, "ID")
                    PrintBasic.print_basic(account_balance_obj.type, "Account Type")
                    PrintBasic.print_basic(account_balance_obj.state, "Account State")
                    PrintBasic.print_basic(account_balance_obj.subtype, "Subtype")
                    account_id = account_balance_obj.id
                    for balance_obj in account_balance_obj.list:
                        if (
                            float(balance_obj.balance) > 0.1
                        ):  # only show account with balance
                            balance_obj.print_object("\t")
                            print()

        LogInfo.output("====== Create Order ======")
        trade_client = TradeClient(api_key=self.g_api_key, secret_key=self.g_secret_key)
        while True:
            try:
                order_id = trade_client.create_order(
                    symbol=self.target_coin,
                    account_id=account_id,
                    order_type=OrderType.BUY_MARKET,
                    source=OrderSource.API,
                    amount=500000,
                    price=0.0001,
                )
                LogInfo.output("created order id : {id}".format(id=order_id))
            except Exception as e:
                print(e)

            time.sleep(1)


if __name__ == "__main__":
    run = Trading_bot()
    run()
