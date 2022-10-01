from re import M
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

"""
================
MAIN MODELS
================
"""
class Walker(models.Model):
    ## Walker/User contact
    name: models.CharField(max_length=20)
    email: models.CharField(max_length=30)
    ##### Walker/User phone number. **** Typing and content may change with call functionality
    phone: models.CharField(max_length=12)

    def __str__(self):
        return f'{self.name}\'s contacts. Email: {self.email}, Phone: {self.phone}'

class Dog(models.Model):
    ## Dog Description
    name: models.CharField(max_length=20)
    breed: models.CharField(max_length=20)
    coatcolor: models.CharField(max_length=15)
    notes: models.TextField(max_length=250)
    ## Owner contact
    ownername: models.CharField(max_length=20)
    ownerphone: models.CharField(max_length=12)
         ### Should ownerADDRESS be changed to TextField?  ****
    owneraddress: models.CharField(max_length=100)
    ## user/walker FK
    user: models.ForeignKey(Walker, on_delete=models.CASCADE)

    """
    ManyToMany field not defined yet
    """

    def __str__(self):
        return f'{self.name}\'s model. FK @ {self.user}'

    def get_absolute_url(self):
        return reverse('dog_detail', kwargs={'dog_id': self.id})

class Activity(models.Model):
    ##Activity info
    date: models.DateField('activity date')
    activity: models.TextField(max_length=250)
    ## dog FK
    dog: models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date}||{self.dog.name}: {self.activity}'

    ### **** Having issues enabling this?
    class Meta:
        # ordering = ['-date']
        pass

"""
=============
Extended Models
=============
"""


"""
*** Need to implement boto3 and environ.
    Need to generate s3 account for bucket
"""
class DogPhoto(models.Model):
    url = models.CharField(max_length=200)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.dog.name}\'s photo  url: {self.url}'


########### Placeholder, may not use at all
class ActivityPhoto(models.Model):
    url = models.CharField(max_length=200)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)