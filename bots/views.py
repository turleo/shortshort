import json

import requests
from django.core.validators import URLValidator
from django.http import HttpResponse
from django.conf import settings
from django.utils import translation

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
                    requests.get(f"https://api.vk.com/method/messages.send?v=5.131&user_id={data['object']['message']['from_id']}&random_id={data['object']['message']['id']}" 
                                     '&message=https://' + request.get_host() + '/' + obj.short(), headers={
                                         'Authorization': f'Bearer {settings.TOKEN_VK}'
                                         })
                    return HttpResponse(b'ok')
                except:
                    requests.get(f"https://api.vk.com/method/messages.send?v=5.131&user_id={data['object']['message']['from_id']}&random_id={data['object']['message']['id']}" 
                                 '&message=Отправьте URL', headers={
                                         'Authorization': f'Bearer {settings.TOKEN_VK}'
                                         })
                    return HttpResponse(b'ok')
            elif data['type'] == 'confirmation':
                return HttpResponse(bytes(settings.CONFORMATION_VK, 'utf8'))
        else:
            return HttpResponse(b'<img src="https://http.cat/403" alt="403 Forbidden"/>', status=403, content_type='text/html')
    else:
        return HttpResponse(b'<img src="https://http.cat/405" alt="405 Method Not Allowed"/>', status=405, content_type='text/html')
    

def tg_bot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if 'text' in data['message']:
            if data['message']['text'] == '/start':
                translation.activate(data['message']['from']['language_code'])
                requests.get(f'https://api.telegram.org/bot{settings.TOKEN_TG}/sendMessage?'
                f'chat_id={data["message"]["from"]["id"]}&text=' + 
                translation.gettext("Send me link and I'll make it shorter ✂"))
                return HttpResponse(b'ok')
            else:
                try:
                    val(data['message']['text'])
                    obj = Link.objects.create(long=data['message']['text'])
                    obj.save()
                    
                    r = requests.get('https://api.telegram.org/bot' + settings.TOKEN_TG + '/sendMessage?chat_id=' + str(data['message']['from']['id']) + '&text=https://' + request.get_host() + '/' + obj.short())
                    print(r.text)

                    return HttpResponse(b'ok')
                except:
                    translation.activate(data['message']['from']['language_code'])
                    requests.get(f'https://api.telegram.org/bot{settings.TOKEN_TG}/sendMessage?chat_id='
                                 f"{data['message']['from']['id']}&text=" + 
                                 translation.gettext('Please, send me valid link 🔗'))
                    print(data['message']['from']['language_code'], translation.get_language())
                    translation.deactivate()
                    return HttpResponse(b'ok')
    else:
        return HttpResponse(b'<img src="https://http.cat/405" alt="405 Method Not Allowed"/>', status=405, content_type='text/html')
