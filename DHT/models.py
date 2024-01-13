from django.db import models
from twilio.rest import Client
# Create your models here.
from django.db import models
import telegram
from django.conf import settings



class Dht11(models.Model):
    temp = models.FloatField(null=True)
    hum = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True,null=True)

    def telegram_bot_sendtext(message):
        send_text = 'https://api.telegram.org/bot' + my_token + '/sendMessage?chat_id=' + my_chat_id + '&parse_mode=MarkdownV2text-' + message

        response = requests.get(send_text)

        return response.json()

    def save(self, *args, **kwargs):
        account_sid = 'AC5549a959e157ad17791dc46c016a5b80'
        auth_token = '19bd82e12e57a96e5a0992be6c559992'
        client = Client(account_sid, auth_token)



        if (self.temp > 10 and self.hum > 20):
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body='Alert ! The temperature and humidity are dangerously high !',
                to='whatsapp:+212771840918'
            )
            print(message.sid)


        elif (self.hum > 20):
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body='Alert ! The humidity is dangerously high !',
                to='whatsapp:+212771840918'
            )
            print(message.sid)

        elif (self.temp > 10 ):
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body='Alert ! The temperature is dangerously high !',
                to='whatsapp:+212771840918'
            )
            print(message.sid)

        return super().save(*args, **kwargs)

