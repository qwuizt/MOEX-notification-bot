
import requests
import json
import datetime
import time
import constants


def get_stock_prices():
    response = requests.get(constants.url, params=constants.params)
    data = json.loads(response.text)
    stock_prices = {}
    for i in range(len(constants.tickers)):
        last_price = data['marketdata']['data'][i][0]
        stock_prices[constants.tickers[i]] = last_price
    return stock_prices


def process_ratio_change(stock_prices, current_ratio, relative_ratio):
    if current_ratio > relative_ratio + constants.threshold:
        message = f"Покупайте {stock_prices[constants.tickers[0]]} и продавайте {stock_prices[constants.tickers[1]]}!"
        message += f"Текущее отношение цен: {current_ratio}"
        constants.bot.send_message(chat_id='YOUR TG CHAT ID', text=message)
        return current_ratio
    elif current_ratio < relative_ratio - constants.threshold:
        message = f"Покупайте {stock_prices[constants.tickers[1]]} и продавайте {stock_prices[constants.tickers[0]]}!"
        message += f"Текущее отношение цен: {current_ratio}"
        constants.bot.send_message(chat_id='YOUR TG CHAT ID', text=message)
        return current_ratio
    return current_ratio


def main():
    opening_time = datetime.time(10, 0)
    closing_time = datetime.time(23, 50)
    break_start_time = datetime.time(18, 40)
    break_end_time = datetime.time(19, 0)
    relative_ratio = constants.relative_ratio
    while True:
        now = datetime.datetime.now().time()
        if (now >= opening_time and now <= break_start_time) or (now >= break_end_time and now <= closing_time):
            stock_prices = get_stock_prices()
            #for i in range(len(constants.tickers)):
            last_price1 = stock_prices[constants.tickers[0]]
            last_price2 = stock_prices[constants.tickers[1]]
            current_ratio = last_price2 / last_price1
            process_ratio_change(stock_prices, current_ratio, relative_ratio)
        if now >= break_start_time and now <= break_end_time:
            time.sleep(60)
        else:
            time.sleep(10)
        relative_ratio = current_ratio

if __name__ == "__main__":
    main()
