# Generated by Django 3.2.25 on 2024-11-24 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0157_alter_issue_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('Medium', 'medium'), ('Critical', 'critical'), ('High', 'high'), ('Low', 'low')], default='low', max_length=10),
        ),
    ]
