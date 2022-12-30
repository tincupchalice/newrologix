from django.db import models


class XymogenApi(models.Model):
    def __str__(self):
        return "{}|{}|{}".format(self.username,
                              self.environment,
                              self.base_url)

    api_id = models.AutoField(primary_key=True)
    environment = models.CharField(max_length=100, default="test")
    base_url = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)


class ShopifyApi(models.Model):
    def __str__(self):
        return "{}|{}".format(self.environment,
                              self.base_url)

    api_id = models.AutoField(primary_key=True)
    environment = models.CharField(max_length=100, default="test")
    base_url = models.CharField(max_length=100, blank=True, null=True)
    access_token = models.CharField(max_length=255, blank=True, null=True)
    key = models.CharField(max_length=255, blank=True, null=True)
    secret_key = models.CharField(max_length=255, blank=True, null=True)

