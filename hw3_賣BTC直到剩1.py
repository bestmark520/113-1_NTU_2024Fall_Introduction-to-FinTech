import ccxt
import time

# 初始化 OKX 交易所，啟用 sandbox 模式
okx = ccxt.okx({
    'apiKey': '',  # API 金鑰
    'secret': '',  # 秘密金鑰
    'password': '',  # 密碼
    'enableRateLimit': True,  # 啟用速率限制
})

# 啟用模擬交易模式
okx.set_sandbox_mode(True)

# 設定交易參數
symbol = 'BTC/USDT'  # 交易對

def fetch_balance():
    """
    獲取帳戶餘額
    返回: (USDT 餘額, BTC 餘額)
    """
    balance = okx.fetch_balance()  # 獲取帳戶餘額
    usdt_balance = balance['total'].get('USDT', 0)  # 獲取 USDT 餘額
    btc_balance = balance['total'].get('BTC', 0)  # 獲取 BTC 餘額
    return usdt_balance, btc_balance

def execute_trade(btc_balance):
    """
    根據 BTC 餘額執行賣出操作
    btc_balance: 當前 BTC 餘額
    """
    if btc_balance > 1:  # 確認 BTC 餘額大於 1
        amount_to_sell = btc_balance - 1  # 賣出 BTC 直到剩下 1
        order = okx.create_market_sell_order(symbol, amount_to_sell)  # 直接賣出剩餘的 BTC
        print(f"賣出: {amount_to_sell} BTC, 訂單詳情: {order}")
    else:
        print("BTC 餘額不足，無法執行賣出操作。")

def main():
    """
    主程序，持續監控市場並根據餘額進行交易
    """
    while True:
        usdt_balance, btc_balance = fetch_balance()  # 獲取餘額
        print(f"當前 USDT 餘額: {usdt_balance}, 當前 BTC 餘額: {btc_balance}")

        execute_trade(btc_balance)  # 根據 BTC 餘額執行賣出
        break  # 直接賣出後結束程式

if __name__ == "__main__":
    main()  # 啟動主程序
