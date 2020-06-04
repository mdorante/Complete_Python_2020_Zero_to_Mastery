import tweepy
import time

auth = tweepy.OAuthHandler('*************************',
                           '**************************************************')
# For OAuthHandler, we pass the consumer API key and Secret key

auth.set_access_token('**************************************************',
                      '*********************************************')
# For set_access_token, we pass the access token and secret token

api = tweepy.API(auth)  # Authenticate and grant access to the Twitter API
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


py_string = 'python'
number_of_tweets = 5


def like_tweets(string, number):
    for tweet in tweepy.Cursor(api.search, string).items(number):
        try:
            tweet.favorite()
            print('I liked this tweet')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break


def follow_back(handle):  # follow back all followers
    for follower in handle(tweepy.Cursor(api.followers).items()):
        follower.follow()


# Like the last 5 tweets containing the string 'python'
like_tweets(py_string, number_of_tweets)

follow_back(limit_handler)
