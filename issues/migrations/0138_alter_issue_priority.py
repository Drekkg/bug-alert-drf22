# Generated by Django 3.2.25 on 2024-11-21 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0137_alter_issue_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('Medium', 'medium'), ('Low', 'low'), ('Critical', 'critical'), ('High', 'high')], default='low', max_length=10),
        ),
    ]
