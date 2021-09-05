# Generated by Django 3.1.2 on 2021-09-05 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_verbose_name_20210118_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpatient',
            name='preferred_contact_method',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.contactmethod', verbose_name='preferred contact method'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='preferred_contact_method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.contactmethod', verbose_name='preferred contact method'),
        ),
    ]
