# Generated by Django 5.1.3 on 2025-01-23 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='techblog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=100)),
                ('discription', models.TextField()),
                ('photo', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
