# Generated by Django 3.2.25 on 2024-11-18 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0068_auto_20241117_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('Medium', 'medium'), ('Critical', 'critical'), ('Low', 'low'), ('High', 'high')], default='low', max_length=10),
        ),
    ]
