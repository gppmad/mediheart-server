from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model

UserModel = get_user_model()

class SignupSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def create(self, validated_data):
        if validated_data["password1"] == validated_data["password2"]:
            user = UserModel.objects.create_user(
                username=validated_data['username'],
                password=validated_data['password1'],
            )
            return user
        else:
            return ("password 1 must be the same of password2 ")


    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "username", "password1", "password2" )