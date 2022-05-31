# Generated by Django 4.0.4 on 2022-05-30 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLShortner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('original_url', models.URLField()),
                ('short_url', models.CharField(max_length=6, unique=True)),
            ],
        ),
    ]
