# Generated by Django 4.1 on 2022-08-13 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
