import tweepy
import time

# consumer_key = 'KoAA60byQNNscezgsP1DpvuKk'
# consumer_secret = 'EgB9mhmfXu9Lmj9sTD5PHziQRENsmSqn1e5Eklc3gdrIySQiSv'
# access_token = '1393204786875482113-q1yU4gF3AoR74alDu5ds33c5FHFtWM'
# access_token_secret = 'WLkOgO8Y4cQ3kpvE7NPMaV3LXf349LwIaClOWGMs31AOq'

authentication = tweepy.OAuthHandler('KoAA60byQNNscezgsP1DpvuKk', 'EgB9mhmfXu9Lmj9sTD5PHziQRENsmSqn1e5Eklc3gdrIySQiSv')
authentication.set_access_token('1393204786875482113-q1yU4gF3AoR74alDu5ds33c5FHFtWM', 'WLkOgO8Y4cQ3kpvE7NPMaV3LXf349LwIaClOWGMs31AOq')

api = tweepy.API(authentication, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

user = api.me()

search = '#FechadoComBolsonaro'
tweetNumbers = 2000

# in_reply_to_status_id = ''

for tweet in tweepy.Cursor(api.search, search).items(tweetNumbers):
    try:
        tweet.retweet()

        # if(tweet.text == '#FechadoComBolsonaro'):
        #     print('Nome do usuário: @' + tweet.user.screen_name)
        #     api.update_status("@" + tweet.user.screen_name + " concordo plenamente com você, gado 🇧🇷 👍 👉", in_reply_to_status_id-tweet.id)
        #     print("Tweet sent successfully.")
        #     print('')

        print('Tweet successfully retweeted.')
        time.sleep(60)

    except tweepy.TweepError as e:
        print('Error: ', e.reason)

    except StopIteration:
        break