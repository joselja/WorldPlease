from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class BlogsSerializer(serializers.Serializer):
    #owner = serializers.ReadOnlyField()
    #name = serializers.CharField()
    #creation_date = serializers.DateTimeField()
    #description = serializers.CharField()
    #image = serializers.FileField()
    #active = serializers.BooleanField
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    description = serializers.CharField()


class UserSerializerList(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField()


class UserSerializer(UserSerializerList):
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    password = serializers.CharField()

    def create(self, validated_data):
        user = User()
        return self.update(user, validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username')
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

    def validate_username(self, username):
        if (self.instance is None or self.instance.username != username) and User.objects.filter(username=username).exists():
            raise ValidationError('Username exists in database')
        return username
