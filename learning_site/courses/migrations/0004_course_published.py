# Generated by Django 3.2.5 on 2021-08-03 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]