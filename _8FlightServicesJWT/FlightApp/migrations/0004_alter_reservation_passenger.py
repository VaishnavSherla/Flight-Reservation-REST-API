# Generated by Django 3.2a1 on 2023-08-05 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FlightApp', '0003_auto_20230805_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FlightApp.passenger'),
        ),
    ]
