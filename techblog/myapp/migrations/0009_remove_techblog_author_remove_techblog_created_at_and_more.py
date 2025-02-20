# Generated by Django 5.1.3 on 2025-02-11 11:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_techblog_author_techblog_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='techblog',
            name='author',
        ),
        migrations.RemoveField(
            model_name='techblog',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='techblog',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.techblog'),
        ),
    ]
