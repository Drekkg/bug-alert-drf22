# Generated by Django 3.2.25 on 2024-11-10 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_projecturl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='projectURL',
            field=models.URLField(blank=True, null=True),
        ),
    ]
