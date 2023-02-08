from django.db import models
from django.contrib.auth.models import AbstractUser


class School(models.Model):
    title = models.CharField('Название школы', max_length=255)

    def __str__(self):
        return f"id:{self.id}, title:{self.title}"


class User(AbstractUser):
    full_name = models.CharField('ФИ', max_length=255, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    prof = models.CharField('Должность', max_length=255)

    def __str__(self):
        return f"id:{self.id}, full_name:{self.full_name}, school:{self.school}, prof:{self.prof}"


class Director(models.Model):
    full_name = models.CharField('ФИ', max_length=255)
    prof = models.CharField('Должность', max_length=255)


class EduLevel(models.Model):
    type = models.CharField('Уровень обучения', max_length=255)

    def __str__(self):
        return f"id:{self.id}, type:{self.type}"


class Proficiency(models.Model):
    level = models.CharField('Знание языка', max_length=255)

    def __str__(self):
        return f"id:{self.id}, level:{self.level}"


class Language(models.Model):
    title = models.CharField('Язык', max_length=255)

    def __str__(self):
        return f"id:{self.id}, title:{self.title}"


class Format(models.Model):
    type = models.CharField('формат', max_length=255)

    def __str__(self):
        return f"id:{self.id}, type:{self.type}"


class Course(models.Model):
    name = models.CharField('Название дисциплины', max_length=255)
    code = models.CharField('Код', max_length=255)

    def __str__(self):
        return f"id:{self.id}, code:{self.code}, name:{self.name}"


class Status(models.Model):
    type = models.CharField('Статус', max_length=255)

    def __str__(self):
        return f"id:{self.id}, type:{self.type}"


class Syllabus(models.Model):
    syllabus_name = models.CharField('Название силлабуса', max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    training_level = models.ForeignKey(EduLevel, on_delete=models.CASCADE, null=True)
    language_of_education = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    proficiency_level = models.ForeignKey(Proficiency, on_delete=models.CASCADE, null=True)
    total_hours = models.IntegerField('Всего часов', null=True)
    classroom_hours = models.IntegerField('Классных часов', null=True)
    iw_hours = models.IntegerField('СРОП часов', null=True)
    prerequisites = models.BooleanField('Пререквизиты', null=True)
    format_of_training = models.ForeignKey(Format, on_delete=models.CASCADE, null=True)
    time_place = models.CharField('Время и место проведения', max_length=255)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    course_objective = models.CharField('Цель курса', max_length=255)
    document = models.FileField('Файл', null=True)
    agreed_with = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"id:{self.id}, syllabus_name:{self.syllabus_name}, course:{self.course}, training_level:{self.training_level}, language_of_education:{self.language_of_education}, proficiency_level:{self.proficiency_level}, total_hours:{self.total_hours}, classrom_hours:{self.classroom_hours}, iw_hours:{self.iw_hours}, prerequisites:{self.prerequisites}, format_of_training:{self.format_of_training}, time_place:{self.time_place}, instructor:{self.instructor}, course_objective:{self.course_objective}, agreed_with:{self.agreed_with}, status: {self.status}"


class Module(models.Model):
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE, null=True)
    week = models.IntegerField('Неделя', null=True)
    theme = models.CharField('Тема', max_length=255)
    format = models.ForeignKey(Format, on_delete=models.CASCADE, null=True)
    tasks = models.CharField('Задания', max_length=255)

    def __str__(self):
        return f"id:{self.id}, syllabus:{self.syllabus}, week:{self.week}, theme:{self.theme}, format:{self.format}, tasks:{self.tasks}"



