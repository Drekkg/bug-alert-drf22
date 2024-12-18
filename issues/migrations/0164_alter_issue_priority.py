# Generated by Django 3.2.25 on 2024-11-24 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0163_alter_issue_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('Medium', 'medium'), ('High', 'high'), ('Critical', 'critical'), ('Low', 'low')], default='low', max_length=10),
        ),
    ]
