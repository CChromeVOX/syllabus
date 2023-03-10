# Generated by Django 4.1.6 on 2023-02-12 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20230208_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.school'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название дисциплины'),
        ),
        migrations.AlterField(
            model_name='user',
            name='prof',
            field=models.CharField(max_length=255, null=True, verbose_name='Должность'),
        ),
    ]
