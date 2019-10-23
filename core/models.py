from django.db import models
from django.contrib.auth.models import User

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

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="doctor")

    hospital = models.ManyToManyField(Hospital, related_name="doctors", verbose_name="Места работы")

    def __str__(self):
        return self.user


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    hospital = models.ManyToManyField(Hospital, related_name='patients', verbose_name="Ваши поликлиники")
