# Generated by Django 2.1.2 on 2018-10-28 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_profile', '0005_auto_20181028_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='doctor_id',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]