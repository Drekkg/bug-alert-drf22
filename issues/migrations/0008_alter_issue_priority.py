# Generated by Django 3.2.25 on 2024-11-11 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0007_alter_issue_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('medium', 'medium'), ('low', 'low'), ('critical', 'critical'), ('high', 'high')], default='low', max_length=10),
        ),
    ]
