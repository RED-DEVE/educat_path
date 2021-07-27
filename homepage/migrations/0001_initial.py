# Generated by Django 2.2.2 on 2021-07-02 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='welcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50)),
                ('hint', models.TextField(max_length=70)),
                ('word', models.CharField(max_length=20)),
                ('HighLight', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='welcome_page')),
            ],
        ),
    ]
