# Generated by Django 2.2.6 on 2019-11-05 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20191023_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form63',
            name='age',
        ),
        migrations.RemoveField(
            model_name='form63',
            name='date',
        ),
        migrations.RemoveField(
            model_name='form63',
            name='doze',
        ),
        migrations.RemoveField(
            model_name='form63',
            name='is_revaccionation',
        ),
        migrations.RemoveField(
            model_name='form63',
            name='result',
        ),
        migrations.RemoveField(
            model_name='form63',
            name='series',
        ),
        migrations.RemoveField(
            model_name='form63',
            name='vaccination_type',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='created',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='updated',
        ),
        migrations.AddField(
            model_name='doctor',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='hospital',
        ),
        migrations.AddField(
            model_name='doctor',
            name='hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, related_name='doctors', to='core.Hospital', verbose_name='Места работы'),
        ),
        migrations.RemoveField(
            model_name='patient',
            name='hospital',
        ),
        migrations.AddField(
            model_name='patient',
            name='hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, related_name='patients', to='core.Hospital', verbose_name='Ваши поликлиники и больницы'),
        ),
        migrations.CreateModel(
            name='TuberculosisVaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age_year', models.IntegerField(default=0)),
                ('age_month', models.IntegerField(blank=True, null=True)),
                ('dose', models.FloatField()),
                ('series', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=255)),
                ('rib', models.CharField(max_length=255)),
                ('form63', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tuberculosis_vaccines', to='core.Form63')),
            ],
        ),
        migrations.CreateModel(
            name='RevactinationAPDTVaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_type', models.IntegerField(choices=[(1, 'АКДС 2 года'), (2, 'АДС 6 лет'), (3, 'АДС-М 11 лет'), (3, 'АДС-М 16 лет'), (3, 'АДС-М 26 лет'), (3, 'АДС-М 36 лет'), (3, 'АДС-М 46 лет'), (3, 'АДС-М 56 лет')])),
                ('date', models.DateField()),
                ('dose', models.FloatField()),
                ('series', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=255)),
                ('reaction', models.CharField(max_length=50)),
                ('denial', models.CharField(max_length=255, verbose_name='Медотвод. Дата и причина')),
                ('note', models.CharField(max_length=255)),
                ('form63', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revactination_APDT_vaccines', to='core.Form63')),
            ],
        ),
        migrations.CreateModel(
            name='PolioVaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_type', models.IntegerField(choices=[(1, 'тОПВ1'), (2, 'тОПВ2'), (3, 'тОПВ3'), (4, 'тОПВ4'), (5, 'ОПВ дополнительный дозы')])),
                ('date', models.DateField()),
                ('dose', models.FloatField()),
                ('series', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=255)),
                ('reaction', models.CharField(max_length=50)),
                ('denial', models.CharField(max_length=255, verbose_name='Медотвод. Дата и причина')),
                ('note', models.CharField(max_length=255)),
                ('form63', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='polio_vaccines', to='core.Form63')),
            ],
        ),
        migrations.CreateModel(
            name='NIDVaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_type', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('date', models.DateField()),
                ('dose', models.FloatField()),
                ('series', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=255)),
                ('reaction', models.CharField(max_length=50)),
                ('denial', models.CharField(max_length=255, verbose_name='Медотвод. Дата и причина')),
                ('form63', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='NID_vaccines', to='core.Form63')),
            ],
        ),
        migrations.CreateModel(
            name='MEPRVaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_type', models.IntegerField(choices=[(1, 'КПК'), (2, 'КК')])),
                ('age', models.IntegerField()),
                ('date', models.DateField()),
                ('dose', models.FloatField()),
                ('series', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=255)),
                ('reaction', models.CharField(max_length=50)),
                ('denial', models.CharField(max_length=255, verbose_name='Медотвод. Дата и причина')),
                ('form63', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MEPR_vaccines', to='core.Form63')),
            ],
        ),
        migrations.CreateModel(
            name='MantouxVaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('dose', models.FloatField()),
                ('series', models.CharField(max_length=50)),
                ('result', models.CharField(max_length=50)),
                ('form63', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mantoux_vaccines', to='core.Form63')),
            ],
        ),
        migrations.CreateModel(
            name='InfectionVaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_type', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('date', models.DateField()),
                ('dose', models.FloatField()),
                ('series', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=255)),
                ('reaction', models.CharField(max_length=50)),
                ('denial', models.CharField(max_length=255, verbose_name='Медотвод. Дата и причина')),
                ('form63', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infection_vaccines', to='core.Form63')),
            ],
        ),
        migrations.CreateModel(
            name='HepatitisBVaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_type', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('dose', models.FloatField()),
                ('series', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=255)),
                ('reaction', models.CharField(max_length=50)),
                ('denial', models.CharField(max_length=255, verbose_name='Медотвод. Дата и причина')),
                ('note', models.CharField(max_length=255)),
                ('form63', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hepatitis_B_vaccines', to='core.Form63')),
            ],
        ),
        migrations.CreateModel(
            name='DTPHHVaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_type', models.IntegerField(choices=[(1, 'АКДОЙГВ+ХИ 51'), (2, 'АКДОВГВ+ХИ Б2'), (3, 'АКДС+ВГВ+ХИБЗ')])),
                ('date', models.DateField()),
                ('dose', models.FloatField()),
                ('series', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=255)),
                ('reaction', models.CharField(max_length=50)),
                ('denial', models.CharField(max_length=255, verbose_name='Медотвод. Дата и причина')),
                ('note', models.CharField(max_length=255)),
                ('form63', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DTPHH_vaccines', to='core.Form63')),
            ],
        ),
    ]
