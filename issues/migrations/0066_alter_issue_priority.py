# Generated by Django 3.2.25 on 2024-11-16 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0065_alter_issue_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('Critical', 'critical'), ('Low', 'low'), ('High', 'high'), ('Medium', 'medium')], default='low', max_length=10),
        ),
    ]
