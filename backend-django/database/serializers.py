from rest_framework import serializers
from .models import Sensor
from .models import Heartbeat
from rest_framework import filters

class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ['serialNumber', 'metadata']

class HeartbeatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Heartbeat
        fields = ['state', 'message']





# class Ml_testSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Ml_test
#         fields = ['email', 'name']


# class Teleconference_transcribeSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Teleconference_transcribe
#         fields = ['filename', 'transcription', 'transcription_baseline']