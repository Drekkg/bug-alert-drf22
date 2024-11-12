# Generated by Django 3.2.25 on 2024-11-12 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_options'),
        ('issues', '0010_auto_20241112_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='issue_project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('low', 'low'), ('medium', 'medium'), ('critical', 'critical'), ('high', 'high')], default='low', max_length=10),
        ),
    ]
