import schedule
import datetime
import exchange_rate
import tweet
import tweepy
import time

def run_weekday_compare():
    day_list = ['월', '화', '수', '목', '금', '토', '일']
    r = datetime.datetime.today().weekday()
    if(day_list[r] == '토' or day_list[r] == '일'):
        print("주말은 Pass!!")
        return None
    else:
        return 1
    
def make_sentence(country="KRW"):
    today_rate = exchange_rate.get_today_exchange(country)
    yester_rate = exchange_rate.get_yesterday_exchange(country)
    if(country=="KRW"):
        sentence = "어제의 환율은{:.2f} 오늘의 환율은 {:.2f}이고, 전일대비 {:.2f}달러, 등락률은 {:.2f}%입니다.".format(yester_rate, today_rate, 
        exchange_rate.compare_yesterday(today_rate, yester_rate), exchange_rate.get_Fluctuation_rate(today_rate, yester_rate))
    else:
        sentence = "昨日の為替レートは{:.2f} 今日の為替レートは{:.2f}であり、前日比{:.2f}ドル、騰落率は{:.2f}％です。".format(yester_rate, today_rate, 
        exchange_rate.compare_yesterday(today_rate, yester_rate), exchange_rate.get_Fluctuation_rate(today_rate, yester_rate))
    return sentence

def start_job():
    COUNTRY = ["KRW", "JPY"]
    try:
        if(run_weekday_compare() == 1):
            api = tweet.login_tweet()
            for co in COUNTRY:
                sentence = make_sentence(co)
                api.update_status(sentence)
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)

schedule.every().day.at("18:00").do(start_job)
while True:
    schedule.run_pending()
    time.sleep(60)