# Generated by Django 3.2.25 on 2024-11-13 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_githubturl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='githubtURL',
            new_name='githubURL',
        ),
    ]
