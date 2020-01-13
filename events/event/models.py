from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.translation import gettext as _

# Create your models here.


class Event(models.Model):
    event_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    event_name=models.CharField(max_length=50)
    event_type=models.CharField(max_length=20)
    no_of_attendees=models.IntegerField()
    event_date=models.DateField(_("Date"),default=datetime.date.today)

class Registration(models.Model):
    registration_id=models.AutoField(primary_key=True)
    event_id=models.ForeignKey(Event,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)


