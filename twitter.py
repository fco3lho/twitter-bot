import tweepy
import time

consumer_key = '' #Insert the key obtained from your Twitter account.
consumer_secret = '' #Insert the key obtained from your Twitter account.
access_token = '' #Insert the key obtained from your Twitter account.
access_token_secret = '' #Insert the key obtained from your Twitter account.

authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)
authentication.set_access_token(access_token, access_token_secret)

api = tweepy.API(authentication, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

user = api.me()

search = '' #Insert the message you want to search for on Twitter.
tweetNumbers = 2000

in_reply_to_status_id = '' #Empty

for tweet in tweepy.Cursor(api.search, search).items(tweetNumbers):
    try:
        tweet.retweet()

        if(tweet.text == search):
            print('Username: @' + tweet.user.screen_name)
            api.update_status("@" + tweet.user.screen_name + "", in_reply_to_status_id-tweet.id) #Message you want to comment on the retweet post.
            print("Tweet sent successfully.")
            print('')

        print('Tweet successfully retweeted.')
        time.sleep(60)

    except tweepy.TweepError as e:
        print('Error: ', e.reason)

    except StopIteration:
        break
