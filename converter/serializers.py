from rest_framework import serializers
from converter.models import converter,signup

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = converter
        fields = ('Todo','Time')
class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = signup
        fields = ('Usr_Id','User_name','Password','Profile_Img')
