# Generated by Django 4.2.2 on 2023-07-10 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('name', models.CharField(max_length=200)),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]