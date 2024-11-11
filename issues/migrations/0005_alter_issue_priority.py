# Generated by Django 3.2.25 on 2024-11-11 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0004_alter_issue_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('critical', 'critical'), ('high', 'high'), ('low', 'low'), ('medium', 'medium')], default='low', max_length=10),
        ),
    ]
