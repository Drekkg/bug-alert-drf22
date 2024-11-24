# Generated by Django 3.2.25 on 2024-11-21 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0152_alter_issue_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('Low', 'low'), ('High', 'high'), ('Critical', 'critical'), ('Medium', 'medium')], default='low', max_length=10),
        ),
    ]