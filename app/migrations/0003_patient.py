# Generated by Django 4.1.2 on 2023-10-30 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_doctor_user_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptname', models.CharField(max_length=250)),
                ('mobileno', models.IntegerField()),
                ('ptime', models.TimeField()),
                ('pdate', models.DateField()),
                ('doctoravail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.doctor')),
            ],
        ),
    ]
