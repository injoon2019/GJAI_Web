# Generated by Django 3.1 on 2020-08-22 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AiClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_num', models.IntegerField()),
                ('teacher', models.CharField(max_length=10)),
                ('class_room', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='AiStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_num', models.IntegerField()),
                ('name', models.CharField(max_length=10)),
                ('phone_num', models.CharField(max_length=10)),
                ('intro', models.TextField()),
            ],
        ),
    ]
