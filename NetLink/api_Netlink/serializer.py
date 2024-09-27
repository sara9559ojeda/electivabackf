from api_Netlink.models import Experience, laboralInformation
from rest_framework import serializers

class laboralInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = laboralInformation
        fields =('id','latestPosition', 'abilities', 'previousExperiences', 'lookingForEmployement', 'desiredPosition', 'desiredCountry', 'telecommuting')

class experienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields =('id','company', 'position', 'description')