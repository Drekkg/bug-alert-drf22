# Generated by Django 3.2.25 on 2024-11-15 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0046_alter_issue_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('Critical', 'critical'), ('Medium', 'medium'), ('Low', 'low'), ('High', 'high')], default='low', max_length=10),
        ),
    ]