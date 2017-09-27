import facebook
import json
import urllib2
api_key = '250999452021399'
app_secret='51569158ac24b06708966fc5c6f59b3d'
acc_token='250999452021399|LtaM8iRmAicRccgNKdP4N72pSl4'
graph = facebook.GraphAPI(access_token='250999452021399|LtaM8iRmAicRccgNKdP4N72pSl4',version='2.6')
graph_url = "https://graph.facebook.com"
profile = graph.get_object(api_key)
post_args = "/Trump/posts/?key=value&access_token=" + acc_token
post_url=graph_url+post_args
resp=urllib2.urlopen(post_url)
json_page=resp.read()
page_final=json.loads(json_page)
print(page_final['data'])











