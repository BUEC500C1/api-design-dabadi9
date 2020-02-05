import tweepy
import key
import json



def get_tweets():
    auth = tweepy.OAuthHandler(key.consumer_key, key.consumer_secret)
    auth.set_access_token(key.access_token, key.access_token_secret)
    tweepy_api = tweepy.API(auth)

    public_tweets = tweepy_api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)
        if 'media' in tweet.entities:
            print("Media:")
            for media in tweet.entities["media"]:
                print(media["media_url"])
        print("")
        print("________________________________________________________________________________________________________________________________________________________________________________________________")
        print("")
        print("")


if __name__ == "__main__":
    get_tweets()
