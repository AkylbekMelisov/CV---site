from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class ResumeView(APIView):
    def get(self, request, *args, **kwarg):
        resume = Resume.objects.all()
        serializer = ResumeSerializer(resume, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': 'OK!'})
        return Response(serializer.errors)


class ExperienceView(APIView):
    def get(self, request, *args, **kwargs):
        experience = Experience.objects.filter(resume__id=kwargs['resume_id'])
        serializer = ExperienceSerializer(experience, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ExperienceCreateSerializer(data=request.data)
        if serializer.is_valid():
            resume = Resume.objects.get(id=kwargs['resume_id'])
            start_date = serializer.data.get('start_date')
            end_date = serializer.data.get('end_date')
            position = serializer.data.get('position')
            company = serializer.data.get('company')
            location = serializer.data.get('location')
            Experience.objects.create(resume=resume, start_date=start_date, end_date=end_date, position=position,
                                      company=company, location=location)
            return Response({'data': 'experience create succesfully!'})
        return Response(serializer.errors)


class EducationView(APIView):
    def get(self, request, *args, **kwargs):
        education = Education.objects.filter(resume__id=kwargs['resume_id'])
        serializer = EducationSerializer(education, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = EducationCreateSerializer(data=request.data)
        if serializer.is_valid():
            resume = Resume.objects.get(id=kwargs['resume_id'])
            start_date = serializer.data.get('start_date')
            end_date = serializer.data.get('end_date')
            type_of_school = serializer.data.get('type_of_school')
            type_of_edu = serializer.data.get('type_of_edu')
            type_of_univer = serializer.data.get('type_of_univer')
            name_of_school = serializer.data.get('name_of_school')
            faculty = serializer.data.get('faculty')
            spec = serializer.data.get('spec')
            Education.objects.create(resume=resume, start_date=start_date, end_date=end_date,
                                     type_of_school=type_of_school, type_of_edu=type_of_edu,
                                     type_of_univer=type_of_univer, name_of_school=name_of_school, faculty=faculty,
                                     spec=spec)
            return Response({'data': 'education create succesfully'})
        return Response(serializer.errors)


class SkillView(APIView):
    def get(self, request, *args, **kwargs):
        skill = Skill.objects.filter(resume__id=kwargs['resume_id'])
        serializer = SkillSerializers(skill, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = SkillCreateSerializer(data=request.data)
        if serializer.is_valid():
            resume = Resume.objects.get(id=kwargs['resume_id'])
            name = serializer.data.get('name')
            star = serializer.data.get('star')
            Skill.objects.create(resume=resume, name=name, star=star)
            return Response({'data': 'skill create succecfully'})
        return Response(serializer.errors)


class LanguageView(APIView):
    def get(self, request, *args, **kwargs):
        language = Language.objects.filter(resume__id=kwargs['resume_id'])
        serializer = LanguageSerializer(language, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = LanguageCreateSerializers(data=request.data)
        if serializer.is_valid():
            resume = Resume.objects.get(id=kwargs['resume_id'])
            name = serializer.data.get('name')
            level = serializer.data.get('level')
            Language.objects.create(resume=resume, name=name, level=level)
            return Response({'data': 'language crate succecfully!'})
        return Response(serializer.errors)
