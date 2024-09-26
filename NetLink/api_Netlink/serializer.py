from api_Netlink.models import Experience, laboralInformation
from rest_framework import serializers

class laboralInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = laboralInformation
        fields =('latestPosition', 'abilities', 'previousExperiences', 'lookingForEmployement', 'desiredPosition', 'desiredCountry', 'telecommuting')

class experienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields =('company', 'position', 'description')