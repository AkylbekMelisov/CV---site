from django.contrib import admin
from .models import *

admin.site.register([Resume, Experience, Education, Skill, Language])
