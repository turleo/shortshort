import json
import random

import requests
import vk
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.http import HttpResponse
from django.shortcuts import render

from links.models import Link

from . import secret

val = URLValidator()


def vk_bot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data['secret'] == secret.secret_vk:
            if data['type'] == 'message_new':
                try:
                    val(data['object']['message']['text'])
                    obj = Link.objects.create(long=data['object']['message']['text'])
                    obj.short = hex(obj.id).split('x')[-1]
                    obj.save()
                    session = vk.Session()
                    api = vk.API(session, v=5.103)
                    user_id = data['object']['message']['from_id']
                            
                    api.messages.send(access_token=secret.token_vk, user_id=str(user_id), message='https://' + request.get_host() + '/' + obj.short, random_id=str(data['object']['message']['id']))

                    return HttpResponse('ok')
                except:
                    session = vk.Session()
                    api = vk.API(session, v=5.103)
                    user_id = data['object']['message']['from_id']
                            
                    api.messages.send(access_token=secret.token_vk, user_id=str(user_id), message="Это не URL", random_id=str(data['object']['message']['id']))
                    return HttpResponse('ok')
            elif data['type'] == 'confirmation':
                return HttpResponse(secret.conformatin_vk)
        else:
            return HttpResponse('<img scr="https://http.cat/403">403 Forbidden</img>', status=403)
    else:
        return HttpResponse('<img scr="https://http.cat/405">405 Method Not Allowed</img>', status=405, content_type='text/html')
    

def tg_bot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if 'text' in data['message']:
            if data['message']['text'] == '/start':
                requests.get('https://api.telegram.org/' + secret.token_tg + '/sendMessage?chat_id=' + str(data['message']['from']['id']) + '&text=Please send me link')
                return HttpResponse('ok')
            else:
                try:
                    val(data['message']['text'])
                    obj = Link.objects.create(long=data['message']['text'])
                    obj.short = hex(obj.id).split('x')[-1]
                    obj.save()
                    
                    requests.get('https://api.telegram.org/' + secret.token_tg + '/sendMessage?chat_id=' + str(data['message']['from']['id']) + '&text=https://' + request.get_host() + '/' + obj.short)

                    return HttpResponse('ok')
                except:                           
                    requests.get('https://api.telegram.org/' + secret.token_tg + '/sendMessage?chat_id=' + str(data['message']['from']['id']) + '&text=Looks lite this isn\'t valid URL 😢')
                    return HttpResponse('ok')
    else:
        return HttpResponse('<img scr="https://http.cat/405">405 Method Not Allowed</img>', status=405, content_type='text/html')
