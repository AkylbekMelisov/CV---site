from rest_framework import serializers
from rest_framework.serializers import Serializer

from .models import *


class ExperienceSerializer(serializers.ModelSerializer):
    resume = serializers.StringRelatedField()
    class Meta:
        model = Experience
        fields = '__all__'


class ExperienceCreateSerializer(Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    position = serializers.CharField(max_length=50)
    company = serializers.CharField(max_length=50)
    location = serializers.CharField(max_length=50)


class EducationSerializer(serializers.ModelSerializer):
    resume = serializers.StringRelatedField()
    class Meta:
        model = Education
        fields = '__all__'


class EducationCreateSerializer(Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    type_of_school = serializers.CharField(max_length=50)
    type_of_edu = serializers.CharField(max_length=50)
    type_of_univer = serializers.CharField(max_length=50)
    name_of_school = serializers.CharField(max_length=50)
    faculty = serializers.CharField(max_length=50)
    spec = serializers.CharField(max_length=50)


class SkillSerializers(serializers.ModelSerializer):
    resume = serializers.StringRelatedField()
    star = serializers.IntegerField(max_value=5, min_value=0)

    class Meta:
        model = Skill
        fields = '__all__'


class SkillCreateSerializer(Serializer):
    name = serializers.CharField(max_length=50)
    star = serializers.IntegerField(max_valie=5, min_value=0)


class LanguageSerializer(serializers.ModelSerializer):
    resume = serializers.StringRelatedField()
    class Meta:
        model = Language
        fields = '__all__'


class LanguageCreateSerializers(Serializer):
    name = serializers.CharField(max_length=50)
    levels = (
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('C1', 'C1'),
        ('C2', 'C2'),
    )
    level = serializers.ChoiceField(levels, default='A1')


class ResumeSerializer(serializers.ModelSerializer):
    experiences = ExperienceSerializer(many=True, required=False)
    educations = EducationSerializer(many=True, required=False)
    skills = SkillSerializers(many=True, required=False)
    languages = LanguageSerializer(many=True, required=False)
    class Meta:
        model = Resume
        fields = '__all__'
