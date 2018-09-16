from rest_framework import serializers
from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password', 'is_staff')
        lookup_field = 'username'
        extra_kwargs = {
            'password': {'write_only': True},
            'url': {'lookup_field': 'username'}
        }
