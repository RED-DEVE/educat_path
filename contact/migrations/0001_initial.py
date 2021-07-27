# Generated by Django 2.2.2 on 2021-07-02 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneOne', models.CharField(max_length=15)),
                ('phoneTwo', models.CharField(max_length=15)),
                ('phoneThree', models.CharField(max_length=15)),
                ('phoneFour', models.CharField(max_length=15)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('face', models.URLField()),
                ('inst', models.URLField()),
                ('tele', models.URLField()),
                ('tup', models.URLField()),
                ('twit', models.URLField()),
                ('workTime', models.TextField(max_length=50)),
                ('workOff', models.TextField(max_length=50)),
                ('about', models.TextField(max_length=100)),
                ('adderess', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=1000)),
                ('message', models.TextField(max_length=2800)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'message from users',
                'verbose_name_plural': 'users message',
            },
        ),
    ]
