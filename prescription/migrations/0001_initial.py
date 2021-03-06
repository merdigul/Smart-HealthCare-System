

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=100)),
                ('days', models.BigIntegerField()),
                ('morning', models.BooleanField(default=True)),
                ('afternoon', models.BooleanField(default=True)),
                ('night', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription_id', models.CharField(max_length=30, unique=True)),
                ('prescription_date', models.DateTimeField(auto_now_add=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='media_/pdf/')),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor_profile.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='prescription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prescription.Prescription'),
        ),
    ]
