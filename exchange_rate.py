import datetime
import config
import requests

def get_yesterday():
    return str(datetime.date.today() - datetime.timedelta(days=1))

def get_Fluctuation_rate(exchange_rate, y_exchange_rate):
    return (exchange_rate-y_exchange_rate)/y_exchange_rate*100

def compare_yesterday(exchange_rate, y_exchange_rate):
    return exchange_rate - y_exchange_rate

def get_today_exchange(country="KRW"): #USD환전 기준
    url = "https://free.currconv.com/api/v7/convert?q=USD_" + country + "&compact=ultra&apiKey=" + config.currency_API
    r = requests.get(url)
    if(r.status_code == 200):
        return r.json()["USD_" + country]
    else:
        print("error")
        exit(1)

def get_yesterday_exchange(country="KRW"):
    yesterday = get_yesterday()
    url = "https://free.currconv.com/api/v7/convert?q=USD_" + country + "&compact=ultra&date=" + yesterday + "&apiKey=" + config.currency_API
    r = requests.get(url)
    if(r.status_code == 200):
        return r.json()["USD_" + country][yesterday]
    else:
        print("error")
        exit(1)

if __name__ == "__main__":
    exchange_rate = get_today_exchange()
    y_exchange_rate = get_yesterday_exchange()
    print("오늘 환율 : {}, 어제 환율 : {}".format(exchange_rate, y_exchange_rate))
    print("오늘의 환율은 {:.2f}이고, 전일대비 {:.2f}달러, 등락률은 {:.2f}%입니다.".format(
        exchange_rate, compare_yesterday(exchange_rate, y_exchange_rate), get_Fluctuation_rate(exchange_rate, y_exchange_rate)))