from django.contrib.auth.models import AbstractUser
from django.db import models
from localflavor.us.us_states import STATE_CHOICES


class CustomUser(AbstractUser):
    company = models.CharField(max_length=255, )
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    zip = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    doctor = models.CharField(max_length=255)
    doctor_phone = models.CharField(max_length=10, blank=True, null=True)
    doctor_email = models.CharField(max_length=255, blank=True, null=True)
    contact1 = models.CharField(max_length=255)
    contact1_phone = models.CharField(max_length=10)
    contact1_email = models.EmailField(max_length=255, blank=True, null=True)
    contact2 = models.CharField(max_length=255, blank=True, null=True)
    contact2_phone = models.CharField(max_length=10, blank=True, null=True)
    contact2_email = models.EmailField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return "{}|{}|{}".format(self.username,
                                 self.company,
                                 self.email)