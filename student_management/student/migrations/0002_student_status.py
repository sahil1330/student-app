# Generated by Django 5.2 on 2025-05-04 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(default='present', max_length=10),
        ),
    ]
