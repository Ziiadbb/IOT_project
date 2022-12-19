import self as self
import telepot
from django.core.mail import send_mail
from django.db import models

# Create your models here.
class Dht(models.Model):
    temp = models.FloatField(null=True)
    hum = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return str(self.temp)

    def save(self, *args, **kwargs):
        if self.temp > 40:
            token = '5726400480:AAFNVHU7XZ8aStl6cCqmzQz06X3WLKDukdc'
            rece_id =2095125904
            bot = telepot.Bot(token)
            bot.sendMessage(rece_id, 'température dépasse la normale,' + str(self.temp))
            print(bot.sendMessage(rece_id, 'OK.'))

            send_mail(
                'température dépasse la normale,' + str(self.temp),
                'anomalie dans la machine',
                'aliou.barry@ump.ac.ma',
                ['ziadbelh17@gmail.com'],
                fail_silently=False,
            )
        return super().save(*args, **kwargs)



