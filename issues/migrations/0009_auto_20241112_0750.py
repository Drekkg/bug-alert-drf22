# Generated by Django 3.2.25 on 2024-11-12 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0008_alter_issue_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='issue_project',
        ),
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('critical', 'critical'), ('low', 'low'), ('high', 'high'), ('medium', 'medium')], default='low', max_length=10),
        ),
    ]