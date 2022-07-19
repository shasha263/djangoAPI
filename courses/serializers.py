from dataclasses import fields
from msilib.schema import Class
from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id','url','name','language','price')