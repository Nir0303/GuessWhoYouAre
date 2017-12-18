import requests
import json
import tweepy
import facebook
import json
import urllib2


# get quora user interests
def get_quora_attributes(uname):
    quora = requests.get("http://quora.christopher.su/users/" + uname + "/activity")
    quora_dict = json.loads(quora.text)
    quora_interests = quora_dict['activity']
    s = ''
    for i in quora_interests:
        s += i['title'] + "\n"
    return s

# get twitter content
def get_twitter_attributes(userName):
    consumer_key = "8GUHQb0KiGZUzJLrVgBxPXwNI"
    consumer_secret = "ZykaLwtwGP0c4JrzlTC9L5iEpaApL0ze9mB7t9mdeSiNa3cTMY"
    access_key = "164930761-F43PD7B9zhTFjhUaWRJGfy4vm825g3XEdlAVO6KH"
    access_secret = "W2LUYCTQPJaRcgPzHY6prtirUFUnod9CI6KCgJq6Ld60F"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    new_tweets = api.user_timeline(screen_name=userName, count=20)
    outtweets = [tweet.text.encode("utf-8") for tweet in new_tweets]
    return outtweets


# get facebook content
def get_facebook_attribute(userName):
    api_key = '250999452021399'
    app_secret = '51569158ac24b06708966fc5c6f59b3d'
    acc_token = '250999452021399|LtaM8iRmAicRccgNKdP4N72pSl4'
    graph = facebook.GraphAPI(access_token='250999452021399|LtaM8iRmAicRccgNKdP4N72pSl4', version='2.6')
    resp = urllib2.urlopen(
        "https://graph.facebook.com" + "/" + userName + "/posts/?key=value&access_token=" + acc_token)
    fb_dict = json.loads(resp.read())['data']
    fb_content = ""
    for i in fb_dict:
        fb_content += i['message'] + "\n"
    return fb_content
