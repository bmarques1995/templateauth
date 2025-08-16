from rest_framework import serializers
from auth_app.models import User

class FullUserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ['name']
    
    def __init__(self, *args, **kwargs):
        kwargs['many'] = kwargs.get('many', True)
        super().__init__(*args, **kwargs)
