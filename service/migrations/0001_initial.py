# Generated by Django 2.2.2 on 2021-07-02 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='service')),
                ('service_name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=80)),
            ],
        ),
    ]
