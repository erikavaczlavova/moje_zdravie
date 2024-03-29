# Generated by Django 4.0.3 on 2022-03-16 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projekt', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('vaccine_id', models.IntegerField()),
                ('date', models.DateTimeField(verbose_name='date of birth')),
                ('dose', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('date', models.DateTimeField(verbose_name='date of birth')),
                ('result', models.BooleanField()),
                ('location', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('date', models.DateTimeField(verbose_name='date of birth')),
                ('dose', models.IntegerField()),
                ('location', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('doctor', models.CharField(max_length=200)),
            ],
        ),
    ]
