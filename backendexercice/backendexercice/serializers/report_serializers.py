from rest_framework import serializers
from backendexercice.models.report import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        exclude = ['created_at', 'updated_at']

