# Generated by Django 4.0.2 on 2022-08-23 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mariga', '0007_projects_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='github',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]