# Generated by Django 2.2.24 on 2021-06-21 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surnames', models.CharField(max_length=100)),
                ('identification_number', models.IntegerField()),
            ],
        ),
    ]