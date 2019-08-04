from rest_framework import serializers
from azureapp.models import QueueModel


class AzureQueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueueModel
        fields = ['queue_uuid', 'message', 'msg_id', 'status']
