from django.db import models


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=100)


class token(models.Model):
    json_token = models.CharField(max_length=300)
