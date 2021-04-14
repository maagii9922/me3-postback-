
from django.http import HttpResponse
from django.views import generic
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import re
import random
import requests


def home(request):
    return HttpResponse("hello")

PAGE_ACCESS_TOKEN = "EAANZA3YNaNMEBAIW4FYwzrnZA9C3NFwZCwXDaGQUUp6wRes2d0p6HJ6ygwLd8HT5ZC04fV3zMGrF9jp3YTvJMjZCvFHaGgZCcPdV27Dvx06qulupKvZBOQCbsBqX7sRYeyabf5K1BOJV6pKUAmCMfcrZCncNG6Ry3R8JIxaKnz3GNgZDZD"
VERIFY_TOKEN='123456'
jokes = {
    u'холбоо барих': [u"""холбоо барих-1.""", u"""холбоо барих-2."""],
    u'түгээмэл асуулт хариулт': [u"""түгээмэл асуулт хариулт-1.""", u"""түгээмэл асуулт хариулт-2"""],
    u'эхлэх': [u"""эхлэх-1""", u"""эхлэх-2."""]
}

class Botview(generic.View):
    def get(self,request, *args,**kwargs):
        if self.request.GET['hub.verify_token']==VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

        
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self,request,*args,**kwargs):
        body=json.loads(self.request.body.decode('utf-8'))
        c=body["entry"][0]["messaging"][0]
        print(c)
        # if "b" in body:
        #     return HttpResponse("bna")
        # else:
        #     return HttpResponse("alga")
        # for key in body:
        #     print(    body[key]             ) 
        # for key in body["c"]:
        #     print(key)
        if "message" in c:
            b=c["message"]
            if "text" in b and "attachments" in b:
                # return HttpResponse("text attachment damjuullaa")
                return HttpResponse(b["text"] + " "+ b["attachments"])                
            elif "attachments" in b and "text" not in b:
                print(b["attachments"])
                # return HttpResponse("attachment damjuullaa")
                # return HttpResponse(b["attachments"])
                sender_psid = c["sender"]["id"]
                d = json.dumps(
                    {"recipient": {"id": sender_psid}, 
                    # "message": {"attachments": "attachments damjuullaa"+b["attachments"]["type"]+b["attachments"]["payload"]["url"]}})
                    "message": {"text": "attachments" }})
                status = requests.post('https://graph.facebook.com/v2.6/me/messages?access_token=%s' % PAGE_ACCESS_TOKEN, headers={ "Content-Type": "application/json"}, data=d)
                return HttpResponse(status)
            elif "text" in b and "attachments" not in b:
                # return HttpResponse("text damjuullaa")
                # return HttpResponse(b["text"])
                sender_psid = c["sender"]["id"]
                d = json.dumps(
                    {"recipient": {"id": sender_psid}, 
                    "message": {"text": "text damjuullaa"+b["text"]}})
                status = requests.post('https://graph.facebook.com/v2.6/me/messages?access_token=%s' % PAGE_ACCESS_TOKEN, headers={ "Content-Type": "application/json"}, data=d)
                return HttpResponse(status)
        elif "postback" in c:
            return HttpResponse(c["postback"]["title"]+" "+c["postback"]["payload"])
            
        

        return HttpResponse("end")






