# Generated by Django 4.1.2 on 2022-11-08 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=30)),
                ('book_id', models.IntegerField()),
                ('book_auth', models.CharField(max_length=30)),
                ('book_copies', models.IntegerField()),
            ],
        ),
    ]
