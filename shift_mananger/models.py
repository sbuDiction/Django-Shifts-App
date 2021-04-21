from django.db import models
from django.utils import timezone
import datetime
# from django.forms import ModelForm
from django import forms

# Create your models here.

WEEK_DAYS = [
    ('Sun', 'Sunday'),
    ('Mon', 'Monday'),
    ('Tue', 'Tuesday'),
    ('Wed', 'Wednesday'),
    ('Thu', 'Thursday'),
    ('Fri', 'Friday'),
    ('Sat', 'Saturday'),
]


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.first_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Shift(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=WEEK_DAYS)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.day

class WeekDays(models.Model):
    day_name = models.CharField(max_length=128)
    


class ShiftForm(forms.Form):
    days = forms.MultipleChoiceField(choices=WEEK_DAYS, widget=forms.CheckboxSelectMultiple)

# ------------------------------------------------------------

class User(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Days(models.Model):
    week_day = models.CharField(max_length=100)
    worker = models.ManyToManyField(User, through='Workers')

    def __str__(self):
        return self.week_day


class Workers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    days = models.ForeignKey(Days, on_delete=models.CASCADE)