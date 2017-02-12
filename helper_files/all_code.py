import requests
import json
import tweepy

##get quora user interests
def getQuoraAttributes():
	quora=requests.get("http://quora.christopher.su/users/Niranjan-Addanki/activity")
	quoraDict = json.loads(quora.text) 
	quoraInterests=quoraDict['activity']
	s=''
	for i in quoraInterests:
		s+=i['title']+"\n"
	return s
quoraContent=getQuoraAttributes()




##get twiter content
def getTwitterAttributes(userName):
	consumer_key = "8GUHQb0KiGZUzJLrVgBxPXwNI"
	consumer_secret = "ZykaLwtwGP0c4JrzlTC9L5iEpaApL0ze9mB7t9mdeSiNa3cTMY"
	access_key = "164930761-F43PD7B9zhTFjhUaWRJGfy4vm825g3XEdlAVO6KH"
	access_secret = "W2LUYCTQPJaRcgPzHY6prtirUFUnod9CI6KCgJq6Ld60F"
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	new_tweets = api.user_timeline(screen_name = userName,count=20)
	outtweets = [tweet.text.encode("utf-8") for tweet in new_tweets]
	return outtweets

	


TwitterContent=' '.join(getTwitterAttributes("J_tsar"))

allContent=quoraContent+TwitterContent

with open('../output/profile.txt','w') as content:
	content.write(allContent)

