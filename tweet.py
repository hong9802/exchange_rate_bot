import tweepy
import config

def login_tweet():
    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECERET)
    api = tweepy.API(auth)
    return api
#api.update_status("test")