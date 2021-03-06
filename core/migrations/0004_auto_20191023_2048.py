# Generated by Django 2.2.2 on 2019-10-23 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191023_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='hospital',
            field=models.ManyToManyField(related_name='doctors', to='core.Hospital', verbose_name='Места работы'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='hospital',
            field=models.ManyToManyField(related_name='patients', to='core.Hospital', verbose_name='Ваши поликлиники и больницы'),
        ),
    ]
