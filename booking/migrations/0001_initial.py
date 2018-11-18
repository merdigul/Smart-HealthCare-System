# Generated by Django 2.0.5 on 2018-11-18 13:01

import booking.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor_profile', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentDetials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viedo_chat_link', models.CharField(max_length=100)),
                ('appointment_id', models.CharField(max_length=20)),
                ('transaction_id', models.CharField(max_length=250)),
                ('doctor_id', models.ForeignKey(blank=True, max_length=250, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor_profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='PaitentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=500)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('mobile_no', models.BigIntegerField()),
                ('symptoms', models.CharField(max_length=250)),
                ('description_of_illness', models.CharField(max_length=250)),
                ('checkout_id', models.CharField(default=booking.models.generateUUID, editable=False, max_length=36, unique=True)),
                ('doctor_id', models.ForeignKey(blank=True, max_length=250, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor_profile.Profile')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='appointmentdetials',
            name='paitent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.PaitentDetails'),
        ),
    ]