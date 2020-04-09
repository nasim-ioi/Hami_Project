from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from .models import Blog


class UserSerializer(serializers.ModelSerializer):
    """ A serializer for creating User objects for users when they
        have signed up. So they can login and get their jwt token. """

    def create(self, validated_data):
        user,_ = User.objects.get_or_create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'password')

        # for hide the inputed password and display bullets instead
        extra_kwargs = { 
            'password' : {
            'style' : {'input_type': 'password'},
            'trim_whitespace' : False,
            'required' : True
            }
        }

        # to make sure passwords are not displayed
        write_only_fields = ('password') 


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'
        
