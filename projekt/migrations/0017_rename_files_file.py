# Generated by Django 4.0.3 on 2022-03-28 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projekt', '0016_rename_file_files'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Files',
            new_name='File',
        ),
    ]
