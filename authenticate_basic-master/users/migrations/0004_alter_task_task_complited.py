# Generated by Django 4.2.3 on 2023-07-19 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_support'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_complited',
            field=models.IntegerField(),
        ),
    ]