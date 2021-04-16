
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
        if "message" in c:
            b=c["message"]
            if "text" in b and "attachments" in b:
                # return HttpResponse("text attachment damjuullaa")
                return HttpResponse(b["text"] + " "+ b["attachments"])                
            elif "attachments" in b and "text" not in b:
                print(b["attachments"][0])
                # return HttpResponse("attachment damjuullaa")
                # return HttpResponse(b["attachments"])
                sender_psid = c["sender"]["id"]
                attachment_url = b["attachments"][0]["payload"]["url"]
                d = json.dumps(
                    {"recipient": {"id": sender_psid}, 
                    "message": {
                        "attachment": {
                            "type": "template",
                            "payload": {
                            "template_type": "generic",
                            "elements": [{
                                "title": "Сайн байна уу Та 'Холбоо барих', 'Түгээмэл асуулт хариулт', 'Эхлэх' дарна уу",
                                "subtitle":"Бидэнтэй холбогдох",
                                "image_url":"https://www.facebook.com/messenger_media?thread_id=100612838351740&attachment_id=186711756628825&message_id=mid.%24cAAABcg0H7yF_CzoJW142fTAHMHM-",
                                "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Эхлэх",
                                    "payload": "home",
                                },
                                {
                                    "type": "postback",
                                    "title": "Холбоо барих",
                                    "payload": "contact",
                                },
                                {
                                    "type": "postback",
                                    "title": "Түгээмэл асуулт хариулт",
                                    "payload": "qa",
                                }
                                ],
                            }]
                            }
                        }
                        }
                    
                    
                    
                    
                    })
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
            print(body["entry"][0]["messaging"][0]["postback"])
            sender_psid = c["sender"]["id"]
            d=""
            if body["entry"][0]["messaging"][0]["postback"]['payload']=='home':
                d = json.dumps(
                    {"recipient": {"id": sender_psid}, 
                    "message": {"text": "home damjuullaa"}})
            elif body["entry"][0]["messaging"][0]["postback"]['payload']=='contact':
                d = json.dumps(
                    {"recipient": {"id": sender_psid}, 
                    "message": {
                        "attachment": {
                            "type": "template",
                            "payload": {
                            "template_type": "generic",
                            "elements": [{
                                "title": "Холбоо барих",
                                "subtitle":"Бид компанийн бүтээгдэхүүн үйлчилгээтэй холбоотой санал хүсэлтийг ажлын өдрүүдэд 8:30-18:00 цагт хүлээн авч шуурхай шийдвэрлэнэ.",
                                "image_url":"https://www.facebook.com/messenger_media?thread_id=100612838351740&attachment_id=164256072246791&message_id=mid.%24cAAABcg0H7yF_Cy_F2142ep8X4GKr",
                                "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Эхлэх",
                                    "payload": "home",
                                }
                                
                                ]
                            },{
                                "title": "Холбоо барих",
                                "subtitle":"Бид компанийн бүтээгдэхүүн үйлчилгээтэй холбоотой санал хүсэлтийг ажлын өдрүүдэд 8:30-18:00 цагт хүлээн авч шуурхай шийдвэрлэнэ.",
                                "image_url":"https://www.facebook.com/messenger_media?thread_id=100612838351740&attachment_id=164256072246791&message_id=mid.%24cAAABcg0H7yF_Cy_F2142ep8X4GKr",
                                "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Эхлэх",
                                    "payload": "home",
                                }
                                ]
                            }
                            
                            ]
                            }
                        }
                        }
                    
                    
                    })

            elif body["entry"][0]["messaging"][0]["postback"]['payload']=='qa':
                d = json.dumps(
                    {"recipient": {"id": sender_psid}, 
                    "message": {
                        "attachment": {
                            "type": "template",
                            "payload": {
                            "template_type": "generic",
                            "elements": [{
                                "title": "Түгээмэл асуулт хариулт",
                                "subtitle":"99221422",
                                "image_url":"https://scontent.xx.fbcdn.net/v/t1.15752-9/173742530_281534720215938_8618674504973062084_n.jpg?_nc_cat=100&ccb=1-3&_nc_sid=58c789&_nc_ohc=aP26TMSylogAX8N1zwB&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=f773c76251565e53f9ff130d5d42ea7a&oe=609D57A2",
                                "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Эхлэх",
                                    "payload": "home",
                                }
                                
                                ]
                            },{
                                "title": "Түгээмэл асуулт хариулт",
                                "subtitle":"96692287",
                                "image_url":"https://scontent.xx.fbcdn.net/v/t1.15752-9/173742530_281534720215938_8618674504973062084_n.jpg?_nc_cat=100&ccb=1-3&_nc_sid=58c789&_nc_ohc=aP26TMSylogAX8N1zwB&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=f773c76251565e53f9ff130d5d42ea7a&oe=609D57A2",
                                "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Эхлэх",
                                    "payload": "home",
                                }
                                ]
                            }
                            
                            ]
                            }
                        }
                        }
                    
                    
                    })


                
            status = requests.post('https://graph.facebook.com/v2.6/me/messages?access_token=%s' % PAGE_ACCESS_TOKEN, headers={ "Content-Type": "application/json"}, data=d)
            return HttpResponse(status)

            
        

        return HttpResponse("end")






