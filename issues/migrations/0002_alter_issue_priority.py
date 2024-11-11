# Generated by Django 3.2.25 on 2024-11-10 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('high', 'high'), ('low', 'low'), ('critical', 'critical'), ('medium', 'medium')], default='low', max_length=10),
        ),
    ]