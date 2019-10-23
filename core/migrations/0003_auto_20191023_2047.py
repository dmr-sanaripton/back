# Generated by Django 2.2.2 on 2019-10-23 14:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191023_1711'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hospital',
            options={'verbose_name': 'Больница', 'verbose_name_plural': 'Больницы'},
        ),
        migrations.AddField(
            model_name='patient',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='blood_type',
            field=models.IntegerField(blank=True, choices=[('1', 'I положительная'), ('2', 'I отрицательная'), ('3', 'II положительная'), ('4', 'II отрицательная'), ('5', 'III положительная'), ('6', 'III отрицательная'), ('7', 'IV положительная'), ('8', 'IV отрицательная')], null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='created',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='hospital',
            field=models.ManyToManyField(blank=True, null=True, related_name='patients', to='core.Hospital', verbose_name='Ваши поликлиники и больницы'),
        ),
        migrations.CreateModel(
            name='Form63',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccination_type', models.CharField(max_length=255)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('age', models.IntegerField()),
                ('series', models.IntegerField()),
                ('doze', models.FloatField()),
                ('result', models.IntegerField(choices=[('1', 'Положительный'), ('2', 'Отрицательный')], default=1)),
                ('is_revaccionation', models.BooleanField(default=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='form63', to='core.Patient')),
            ],
            options={
                'verbose_name': 'Форма 63 - Карта профилактических прививок',
                'verbose_name_plural': 'Форма 63 - Карта профилактических прививок',
            },
        ),
    ]