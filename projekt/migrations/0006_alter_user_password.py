# Generated by Django 4.0.3 on 2022-03-24 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projekt', '0005_alter_user_height_alter_user_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
