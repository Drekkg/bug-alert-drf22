# Generated by Django 3.2.25 on 2024-11-12 14:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_options'),
        ('issues', '0014_issue_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='issue',
            name='console_error',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='issue',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='issue',
            name='issue_project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
        ),
        migrations.AddField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('medium', 'medium'), ('low', 'low'), ('high', 'high'), ('critical', 'critical')], default='low', max_length=10),
        ),
        migrations.AddField(
            model_name='issue',
            name='repeatable',
            field=models.BooleanField(default=False),
        ),
    ]
