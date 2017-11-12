from django.contrib import admin
from .models import Hacker, Repository, BasicInfo, SkillSet


# Register your models here.
admin.site.register(Hacker)
admin.site.register(Repository)
admin.site.register(BasicInfo)
admin.site.register(SkillSet)
