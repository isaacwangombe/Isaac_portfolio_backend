# Generated by Django 4.0.2 on 2022-08-15 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mariga', '0003_alter_databases_database_alter_frameworks_framework_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='database',
            field=models.ManyToManyField(blank=True, null=True, to='mariga.Databases'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='frameworks',
            field=models.ManyToManyField(blank=True, null=True, to='mariga.Frameworks'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='tools',
            field=models.ManyToManyField(blank=True, null=True, to='mariga.Tools'),
        ),
    ]
