
import tweepy

from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

twts = api.search(q="Make America Great Again")

#list of specific strings we want to check for in Tweets
t = ['Make America Great Again']

sent = False

for s in twts:
    for i in t:
        if i in s.text and 'realDonaldTrump' in s.text and not sent:
            sn = s.user.screen_name
            m = "@%s I pity da foo! https://goo.gl/9dbcUQ" % (sn)
            s = api.update_status(m, s.id)
            sent = True
