from django.db import models
from django.urls import reverse

from celery import shared_task

@shared_task
def hello_there_async():
    print("Hello there")


def hello_there():
    hello_there_async.delay()
    
# Create your models here.
class Shelter(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Dog(models.Model):
    shelter = models.ForeignKey(Shelter, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    description = models.TextField()
    intake_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('dog_detail', args=[str(self.id)])
