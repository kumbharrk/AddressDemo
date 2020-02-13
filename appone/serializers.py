from rest_framework.serializers import ModelSerializer
from appone.models import StudInfo,Address

class StudentSer(ModelSerializer):
    class Meta:
        model =StudInfo
        fields = '__all__'


class AddressSer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'