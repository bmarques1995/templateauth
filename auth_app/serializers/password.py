from rest_framework import serializers
from auth_app.models import Password

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model= Password
        fields= ['user_idx', 'password_hash']
    
    def __init__(self, *args, **kwargs):
        kwargs['many'] = kwargs.get('many', True)
        super().__init__(*args, **kwargs)

class PasswordReseterSerializer(serializers.ModelSerializer):
    class Meta:
        model= Password
        fields= ['password_hash']

    def __init__(self, *args, **kwargs):
        kwargs['many'] = kwargs.get('many', True)
        super().__init__(*args, **kwargs)
