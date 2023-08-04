import json
import random

import requests
import vk
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

from links.models import Link

val = URLValidator()


def vk_bot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data['secret'] == settings.SECRET_VK:
            if data['type'] == 'message_new':
                try:
                    val(data['object']['message']['text'])
                    obj = Link.objects.create(long=data['object']['message']['text'])
                    obj.save()
                    session = vk.Session()
                    api = vk.API(session, v=5.103)
                    user_id = data['object']['message']['from_id']
                            
                    api.messages.send(access_token=settings.SECRET_VK, user_id=str(user_id), message='https://' + request.get_host() + '/' + obj.short(), random_id=str(data['object']['message']['id']))

                    return HttpResponse(b'ok')
                except:
                    session = vk.Session()
                    api = vk.API(session, v=5.103)
                    user_id = data['object']['message']['from_id']
                            
                    api.messages.send(access_token=settings.TOKEN_VK, user_id=str(user_id), message="Это не URL", random_id=str(data['object']['message']['id']))
                    return HttpResponse(b'ok')
            elif data['type'] == 'confirmation':
                return HttpResponse(bytes(settings.CONFORMATON_VK, 'utf8'))
        else:
            return HttpResponse(b'<img src="https://http.cat/403" alt="403 Forbidden"/>', status=403, content_type='text/html')
    else:
        return HttpResponse(b'<img src="https://http.cat/405" alt="405 Method Not Allowed"/>', status=405, content_type='text/html')
    

def tg_bot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if 'text' in data['message']:
            if data['message']['text'] == '/start':
                requests.get('https://api.telegram.org/' + settings.TOKEN_TG + '/sendMessage?chat_id=' + str(data['message']['from']['id']) + '&text=Please send me link')
                return HttpResponse(b'ok')
            else:
                try:
                    val(data['message']['text'])
                    obj = Link.objects.create(long=data['message']['text'])
                    obj.save()
                    
                    requests.get('https://api.telegram.org/' + settings.TOKEN_TG + '/sendMessage?chat_id=' + str(data['message']['from']['id']) + '&text=https://' + request.get_host() + '/' + obj.short())

                    return HttpResponse(b'ok')
                except:
                    requests.get('https://api.telegram.org/' + settings.TOKEN_TG + '/sendMessage?chat_id=' + str(data['message']['from']['id']) + '&text=Looks lite this isn\'t valid URL 😢')
                    return HttpResponse(b'ok')
    else:
        return HttpResponse(b'<img src="https://http.cat/405" alt="405 Method Not Allowed"/>', status=405, content_type='text/html')
