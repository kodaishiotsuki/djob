from rest_framework import serializers

from .models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'id',
            'title',
            'position_salary',
            'position_location',
            'company_name',
            'creaed_at_formatted',
        )
