# Generated by Django 3.2.6 on 2021-11-13 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='images/static/users/profile/profile2_suxx5z.png', null=True, upload_to='static/users/profile'),
        ),
    ]