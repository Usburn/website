# Generated by Django 5.2 on 2025-05-13 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_author_user_project_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
    ]
