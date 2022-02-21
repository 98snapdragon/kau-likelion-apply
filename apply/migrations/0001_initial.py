# Generated by Django 4.0.2 on 2022-02-21 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('studentId', models.CharField(max_length=20)),
                ('grade', models.CharField(max_length=10)),
                ('major', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=20)),
                ('motive', models.TextField(max_length=499)),
                ('position', models.CharField(max_length=10)),
                ('positionRe', models.TextField(max_length=499)),
                ('teamwork', models.TextField(max_length=499)),
                ('passion', models.TextField(max_length=499)),
                ('code', models.TextField(max_length=499)),
            ],
        ),
    ]
