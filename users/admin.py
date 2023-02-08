from django.contrib import admin
from users.models import *
from django.contrib.auth.admin import UserAdmin


class MainAdmin(UserAdmin):
    pass


admin.site.register(User, MainAdmin)
admin.site.register(School)
admin.site.register(Director)
admin.site.register(EduLevel)
admin.site.register(Proficiency)
admin.site.register(Language)
admin.site.register(Course)
admin.site.register(Status)
admin.site.register(Syllabus)
admin.site.register(Module)

