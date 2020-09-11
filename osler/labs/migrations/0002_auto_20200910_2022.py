# Generated by Django 3.0.5 on 2020-09-11 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200910_2022'),
        ('labs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Lab',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Patient'),
        ),
    ]
