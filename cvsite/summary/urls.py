from django.urls import path
from .views import *

urlpatterns = [
    path('', ResumeView.as_view()),
    path('experience/<int:resume_id>/', ExperienceView.as_view()),
    path('education/<int:resume_id>/', EducationView.as_view()),
    path('skill/<int:resume_id>/', SkillView.as_view()),
    path('language/<int:resume_id>/', LanguageView.as_view())
]
