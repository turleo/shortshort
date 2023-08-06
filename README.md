# <img src="static/logo.svg" height="32px"/> ShortShort
This is a simple link shortener, which I wrote to practice in Django and webhooks.

[Web version](https://shortshort.pythonanywhere.com/)

[Telegram bot](https://shortshort.pythonanywhere.com/4)

[VK (🤮) bot](https://shortshort.pythonanywhere.com/5)
## How to run

1. Clone
2. Install packages
``` bash
pip install -r requirements.txt
```
3. Write configuration to `.env` file
``` bash
SECRET_KEY="Secret key for django"
ALLOWED_HOST="Domain name/IP address of your ShortShort instance"
```
4. Create database 
``` bash
python manage.py makemigrations
python manage.py migrate
```
5. Run it
```bash
python manage.py runserver
```
### Telegram bot
To run telegram bot you need to add token form [BotFather](https://t.me/BotFather) to `.env` file
``` bash
TOKEN_TG="Telegram bot token from BotFather"
```
Also, you have to set up webhook manually. To do it follow this link:
```
https://api.telegram.org/bot{Your bot token}/setWebhook?url=https://{Your bot domain}/bots/tg/
```
You will receive JSON file.
### VK (🤮) bot
You have to add this values into your `.env` file. You can find instruction for first two values [here](https://dev.vk.com/ru/api/callback/getting-started) and for third value [here](https://dev.vk.com/ru/api/access-token/getting-started#%D0%9A%D0%BB%D1%8E%D1%87%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%B0%20%D1%81%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%B0)
```
SECRET_VK="Secret key for VK"
CONFORMATION_VK="Conformation for vk, to approve your webhook"
TOKEN_VK="Access token for your VK bot"
```

# Screenshots
![Web](media/web.gif)
![Telegram](media/telegram.gif)

