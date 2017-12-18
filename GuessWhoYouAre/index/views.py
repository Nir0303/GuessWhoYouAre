from django.http import HttpResponse
import os
from .models import Networks
from django.template import loader
from django.shortcuts import render
import time
import social_media
import personal_insights


def index(request):
    return render(request,'index/index.html')

def trait(request):
    user_attributes =request.POST
    quoraContent = social_media.get_quora_attributes(user_attributes['qname'])
    twitterContent = ' '.join(social_media.get_twitter_attributes(user_attributes['twtname']))
    fbContent=social_media.get_facebook_attribute(user_attributes['fbname'])
    with open('output\\profile.txt', 'w') as content:
        content.write(quoraContent.encode('utf-8'))
        time.sleep(5)
        content.write('\n')
        content.write(twitterContent.encode('utf-8'))
        time.sleep(5)
        content.write('\n')
        content.write(fbContent.encode('utf-8'))
        time.sleep(5)
    personal_insights.traits()
    return render(request, 'index/traits.html')