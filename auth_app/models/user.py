from django.db import models
from django_mysql.models import EnumField
from auth_app.fields.byte_stream import ByteStreamField

class User(models.Model):
    # class UserType(models.TextChoices):
    #     COMMON = "common"
    #     COMPANY = "company"

    # class UserSubscription(models.TextChoices):
    #     OWN = "own"
    #     GOOGLE = "google"

    name = models.CharField(max_length=255, primary_key=True)
