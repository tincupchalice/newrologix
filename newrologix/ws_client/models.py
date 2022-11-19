from django.db import models
from localflavor.us.us_states import STATE_CHOICES


class Client(models.Model):
    def __str__(self):
        return "{}|{}|{}|{}|{}|{}|".format(self.client_company,
            self.client_city, self.client_state,
            self.client_doctor, self.client_contact1,
            self.client_phone[0:3] + "." + self.client_phone[4:7] + "." + self.client_phone[7:])

    client_id = models.AutoField(primary_key=True)
    client_company = models.CharField(max_length=255,)
    client_address1 = models.CharField(max_length=255)
    client_address2 = models.CharField(max_length=255, null=True, blank=True)
    client_city = models.CharField(max_length=255)
    client_state = models.CharField(max_length=2, choices=STATE_CHOICES)
    client_zip = models.CharField(max_length=10)
    client_phone = models.CharField(max_length=10)
    client_email = models.CharField(max_length=255)
    client_doctor = models.CharField(max_length=255)
    client_doctor_phone = models.CharField(max_length=10, blank=True, null=True)
    client_doctor_email = models.CharField(max_length=255, blank=True, null=True)
    client_contact1 = models.CharField(max_length=255)
    client_contact1_phone = models.CharField(max_length=10)
    client_contact1_email = models.CharField(max_length=255, blank=True, null=True)
    client_contact2 = models.CharField(max_length=255, blank=True, null=True)
    client_contact2_phone = models.CharField(max_length=10, blank=True, null=True)
    client_contact2_email = models.CharField(max_length=255, blank=True, null=True)
