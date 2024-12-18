# Generated by Django 3.2.25 on 2024-11-12 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0019_alter_issue_priority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='issue_project',
            new_name='issue_project_id',
        ),
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('Low', 'low'), ('Medium', 'medium'), ('Critical', 'critical'), ('High', 'high')], default='low', max_length=10),
        ),
    ]
