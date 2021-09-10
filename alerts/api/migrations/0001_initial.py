# Generated by Django 2.2 on 2020-10-10 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wieght',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('install_ts', models.DateTimeField(auto_now_add=True)),
                ('update_ts', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=300)),
                ('total_wieght', models.IntegerField()),
                ('wieght', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
