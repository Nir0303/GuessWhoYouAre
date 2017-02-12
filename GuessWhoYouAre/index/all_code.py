import requests
import json
import tweepy
import facebook
import json
import urllib2


# get quora user interests
def getQuoraAttributes(uname):
    quora = requests.get("http://quora.christopher.su/users/" + uname + "/activity")
    quoraDict = json.loads(quora.text)
    quoraInterests = quoraDict['activity']
    s = ''
    for i in quoraInterests:
        s += i['title'] + "\n"
    return s

# get twitter content
def getTwitterAttributes(userName):
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
def getFaceBookAttribute(userName):
    api_key = '250999452021399'
    app_secret = '51569158ac24b06708966fc5c6f59b3d'
    acc_token = '250999452021399|LtaM8iRmAicRccgNKdP4N72pSl4'
    graph = facebook.GraphAPI(access_token='250999452021399|LtaM8iRmAicRccgNKdP4N72pSl4', version='2.6')
    resp = urllib2.urlopen(
        "https://graph.facebook.com" + "/" + userName + "/posts/?key=value&access_token=" + acc_token)
    fbDict = json.loads(resp.read())['data']
    fbContent = ""
    for i in fbDict:
        fbContent += i['message'] + "\n"
    return fbContent
