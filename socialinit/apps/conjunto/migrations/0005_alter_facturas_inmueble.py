# Generated by Django 4.2.5 on 2023-09-22 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conjunto', '0004_alter_tar_inm_fechafin_alter_tar_inm_fechainicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturas',
            name='inmueble',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conjunto.inmuebles'),
        ),
    ]
