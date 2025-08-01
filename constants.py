import telebot


# инициализация бота
bot = telebot.TeleBot("YOUR BOT TOKEN")

# тикер акции, котировки которой будем получать (н.п SBER)
tickers = [' ', ' '] 

# URL для получения котировок
url = 'https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities.json'

# параметры запроса
params = {
    'iss.meta': 'off',
    'iss.only': 'securities,marketdata',
    'securities':",".join(tickers),
    'marketdata.columns': 'LAST'
}


# отношение цены ticker1 к цене ticker2
relative_ratio = 1

# количество пунктов на которое меняется соотношение активов 
# для срабатывания условия покупки/продажи
threshold = 1