# Generated by Django 3.2.25 on 2024-11-20 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0105_alter_issue_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('High', 'high'), ('Low', 'low'), ('Medium', 'medium'), ('Critical', 'critical')], default='low', max_length=10),
        ),
    ]
