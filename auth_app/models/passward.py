from django.db import models
from auth_app.fields.byte_stream import ByteStreamField
from .user import User

class Password(models.Model):
    user_idx = models.OneToOneField(to=User, on_delete=models.CASCADE)
    password_hash = ByteStreamField(stream_size=60, null=False)
