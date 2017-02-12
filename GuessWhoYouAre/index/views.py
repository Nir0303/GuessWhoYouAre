from django.http import HttpResponse
import os
from .models import Networks
from django.template import loader
from django.shortcuts import render
import time
import all_code
import personal_insights


def index(request):
    #template = loader.get_template('index/index.html')
    #return HttpResponse(template.render(request))
    return render(request,'index/index.html')

def trait(request):
    if(True):
        print request.POST
        #return HttpResponse("test")
        userAttributes =request.POST
        print userAttributes['qname'],userAttributes['twtname'],userAttributes['fbname']
        quoraContent = all_code.getQuoraAttributes(userAttributes['qname'])
        twitterContent = ' '.join(all_code.getTwitterAttributes(userAttributes['twtname']))
        fbContent=all_code.getFaceBookAttribute(userAttributes['fbname'])
        allContent = quoraContent+ twitterContent + fbContent
        with open('output\\profile.txt', 'w') as content:
            content.write(quoraContent.encode('utf-8'))
            time.sleep(5)
            content.write('\n')
            content.write(twitterContent.encode('utf-8'))
            time.sleep(5)
            content.write('\n')
            content.write(fbContent.encode('utf-8'))
            time.sleep(5)
    else:
        pass
    #return HttpResponse(personal_insights.traits())
    personal_insights.traits()
    print os.getcwd()
    return render(request, 'index/traits.html')