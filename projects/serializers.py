from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Project
        fields = ('id', 'title', 'description', 'technology', 'crated_at')
        read_only_fields = ('crated_at',)
