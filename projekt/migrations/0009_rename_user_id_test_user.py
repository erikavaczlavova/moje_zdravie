# Generated by Django 4.0.3 on 2022-03-28 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projekt', '0008_alter_test_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='user_id',
            new_name='user',
        ),
    ]
