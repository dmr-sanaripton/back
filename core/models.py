from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Hospital(models.Model):
    name = models.CharField(max_length=255)

    region = models.IntegerField(
        choices=(
            (1, ("Бишкек")),
            (2, ("Чуйская область")),
            (3, ("Ошская область")),
            (4, ("Нарынская область")),
            (5, ("Жалал-Абадская область")),
            (6, ("Баткенская область")),
            (7, ("Иссык-Кульская область")),
            (8, ("Таласская область"))),
        default=1)

    address = models.CharField(max_length=255, verbose_name="Адрес", null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Больница"
        verbose_name_plural = "Больницы"

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="doctor")

    hospital = models.ManyToManyField(
        to=Hospital, related_name="doctors",
        verbose_name="Места работы")

    def __str__(self):
        return self.user.username


class Patient(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='patient')
    address = models.CharField(max_length=255, null=True, blank=True) 
    birth_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True, null=True, blank=True) 
    updated = models.DateTimeField(auto_now_add=True, null=True, blank=True) 
    blood_type = models.IntegerField(
        choices=(
            ('1', 'I положительная'),
            ('2', 'I отрицательная'),
            ('3', 'II положительная'),
            ('4', 'II отрицательная'),
            ('5', 'III положительная'),
            ('6', 'III отрицательная'),
            ('7', 'IV положительная'),
            ('8', 'IV отрицательная'),
            ), null=True, blank=True
    )   

    hospital = models.ManyToManyField(
        to=Hospital, related_name='patients',
        verbose_name="Ваши поликлиники и больницы")

    def __str__(self):
        return self.user.username


class Form63(models.Model):
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE, related_name='form63')
    vaccination_type = models.CharField(max_length=255)
    date = models.DateField(default=now)
    age = models.IntegerField()
    series = models.IntegerField()
    doze = models.FloatField()
    result = models.IntegerField(choices=((1, ('Положительный')), (2, ('Отрицательный'))), default=2)
    is_revaccionation = models.BooleanField(default=True)   
    
    class Meta:
        verbose_name = "Форму 63"
        verbose_name_plural = "Форма 63 - Карта профилактических прививок"

    def __str__(self):
        return self.patient.user.username