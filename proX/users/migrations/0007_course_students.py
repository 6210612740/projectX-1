# Generated by Django 3.2.8 on 2021-10-29 14:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_course_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='courses', to=settings.AUTH_USER_MODEL),
        ),
    ]