from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=250)
    choice_one = models.CharField(max_length=100, null=True)
    choice_two = models.CharField(max_length=100, null=True)
    choice_three = models.CharField(max_length=100, null=True)
    choice_one_count = models.IntegerField(default=0, null=True)
    choice_two_count = models.IntegerField(default=0, null=True)
    choice_three_count = models.IntegerField(default=0, null=True)

    def __str__(self):
        return f'{self.question}: ({self.choice_one}, {self.choice_two}, {self.choice_three})'
    
    def get_absolute_url(self):
        return reverse('polls_detail', kwargs={'poll_id': self.id})

class Event(models.Model):
    name = models.CharField(max_length=100)
    who = models.CharField(max_length=150)
    what = models.CharField(max_length=150)
    where = models.CharField(max_length=100)
    when = models.CharField(max_length=150)
    why = models.TextField(max_length=250)
    # will need to uncomment this once the superuser/admin access is created
    # adds a user_id foreignkey colum in the DB
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # class Meta:
    #     ordering = ['-date']
    # creates a Many to Many Relationship with Poll model
    polls = models.ManyToManyField(Poll)

    def __str__(self):
        return self.what

    def get_absolute_url(self):
        return reverse('detail', kwargs={'event_id': self.id})




class Group(models.Model):
    name = models.CharField(max_length=50)
    creator = models.CharField(max_length=100)
    # will need to uncomment this once the superuser/admin access is created
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('groups_index')
