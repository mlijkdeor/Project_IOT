from django.db import models
from twilio.rest import Client
# Create your models here.
from django.db import models
class Dht11(models.Model):
    temp = models.FloatField(null=True)
    hum = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True,null=True)

    def save(self, *args, **kwargs):
        account_sid = 'AC5549a959e157ad17791dc46c016a5b80'
        auth_token = 'a0405ac2d7c6992fe00a3f8193008deb'
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

