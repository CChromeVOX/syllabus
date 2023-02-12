from django import forms
from django.forms import ModelForm
from.models import Syllabus, Module


class SyllabusForm(ModelForm):
    class Meta:
        model = Syllabus
        fields = ['syllabus_name', 'course', 'training_level', 'language_of_education', 'proficiency_level', 'total_hours', 'classroom_hours', 'iw_hours', 'prerequisites', 'format_of_training', 'time_place', 'course_objective', 'agreed_with']

class ModulesForm(ModelForm):
    class Meta:
        model = Module
        fields = ['week', 'theme', 'format', 'tasks']