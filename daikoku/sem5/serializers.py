from rest_framework import serializers
from sem5.models import uscore
from django.contrib.auth.models import User

class uscoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = uscore
        feild=(
               'index',
               'username_id',
               'lvl',
               'best',
               'avg'
        )
