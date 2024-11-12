# Generated by Django 3.2.25 on 2024-11-12 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0015_auto_20241112_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('high', 'high'), ('critical', 'critical'), ('low', 'low'), ('medium', 'medium')], default='low', max_length=10),
        ),
    ]
