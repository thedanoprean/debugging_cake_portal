from rest_framework import serializers
from topic.models.topic_model import Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['title', 'post', 'tag']

