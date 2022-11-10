from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """Users profile"""
    PHYSICAL = 'PH'
    LEGAL = 'L'

    CHOICES = [
        (PHYSICAL, 'Физ. лицо'),
        (LEGAL, 'Юр. лицо'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    post_code = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=255, blank=True)
    region = models.CharField(max_length=255, blank=True)
    area = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    street = models.CharField(max_length=255, blank=True)
    building = models.CharField(max_length=10, blank=True)

    @property
    def address(self):
        return f'{self.country}, {self.region}, {self.area}, {self.city}, ' \
               f'{self.street}, {self.building}'
