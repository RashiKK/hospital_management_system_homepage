# Generated by Django 4.2.6 on 2023-10-27 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_timing_doctor_timings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='timings',
        ),
        migrations.AddField(
            model_name='timing',
            name='doctor',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='timings', to='homepage.doctor'),
            preserve_default=False,
        ),
    ]
