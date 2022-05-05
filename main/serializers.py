<<<<<<< HEAD
=======
import email

>>>>>>> 0e4b74dbfe5c43681675f4b7d7a9973061847952
from rest_framework import serializers
from .models import (
<<<<<<< HEAD
    User,
=======
    Article,
    Category,
    Presentation,
>>>>>>> 0e4b74dbfe5c43681675f4b7d7a9973061847952
    Comment
)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

        extra_kwargs = {'password' : {
            'write_only' : True,
            'required': True
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
<<<<<<< HEAD
=======
        model = Presentation
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
>>>>>>> 0e4b74dbfe5c43681675f4b7d7a9973061847952
        model = Comment
        fields = ('commenter_name', 'comment_body')
