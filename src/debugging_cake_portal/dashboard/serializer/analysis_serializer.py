from rest_framework import serializers
from dashboard.models import Analysis


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = ['nr_users', 'nr_comments', 'nr_posts']
