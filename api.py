import tweepy
import key
import json
from flask import Flask
from flask_restful import Resource, Api
from google.cloud import vision

app = Flask(__name__)
api = Api(app)


def detect_labels_uri(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations

    response = {}
    i = 0

    for label in labels:
        response[i] = label.description
        i = i + 1

    return response    


class GetTweets(Resource):
    def get(self):
        auth = tweepy.OAuthHandler(key.consumer_key, key.consumer_secret)
        auth.set_access_token(key.access_token, key.access_token_secret)
        tweepy_api = tweepy.API(auth)

        public_tweets = tweepy_api.home_timeline()

        tweets = []

        for tweet in public_tweets:
            append_tweet = {'text': tweet.text}

            if 'media' in tweet.entities:
                append_tweet['media'] = []
                for media in tweet.entities["media"]:
                    append_tweet['media'].append(detect_labels_uri(media["media_url"]))
            tweets.append(append_tweet)

        return tweets


api.add_resource(GetTweets, '/')

if __name__ == "__main__":
    app.run(debug=True)
