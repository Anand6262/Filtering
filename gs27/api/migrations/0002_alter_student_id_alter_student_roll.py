# Generated by Django 4.0.6 on 2022-09-09 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(unique=True),
        ),
    ]
