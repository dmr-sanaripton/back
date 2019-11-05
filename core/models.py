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

    hospital = models.ForeignKey(
        to=Hospital, on_delete=None,related_name="doctors",
        verbose_name="Места работы", null=True, blank=True)
    
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Patient(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='patient')
    address = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
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

    hospital = models.ForeignKey(
        to=Hospital, on_delete=None, related_name='patients',
        verbose_name="Ваши поликлиники и больницы",
        null=True, blank=True)

    def __str__(self):
        return self.user.username


class Form63(models.Model):
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE, related_name='form63')
    
    class Meta:
        verbose_name = "Форму 63"
        verbose_name_plural = "Форма 63 - Карта профилактических прививок"

    def __str__(self):
        return self.patient.user.username


class TuberculosisVaccine(models.Model):
    form63 = models.ForeignKey(Form63, on_delete=models.CASCADE, related_name="tuberculosis_vaccines") 
    name = models.CharField(max_length=255)
    age_year = models.IntegerField(default=0)
    age_month = models.IntegerField(null=True, blank=True)
    dose = models.FloatField()
    series = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=255)	 
    rib = models.CharField(max_length=255)	

    def __str__(self):
        return self.form63.patient.user.username


class MantouxVaccine(models.Model):
    form63 = models.ForeignKey(Form63, on_delete=models.CASCADE, related_name="mantoux_vaccines") 
    date = models.DateField()
    dose = models.FloatField()
    series = models.CharField(max_length=50)
    result = models.CharField(max_length=50)

    def __str__(self):
        return self.form63.patient.user.username


class HepatitisBVaccine(models.Model):
    form63 = models.ForeignKey(Form63, on_delete=models.CASCADE, related_name="hepatitis_B_vaccines")
    vaccine_type = models.CharField(max_length=50)
    date = models.DateField()
    dose = models.FloatField() 
    series = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=255)	
    reaction = models.CharField(max_length=50)
    denial = models.CharField("Медотвод. Дата и причина", max_length=255)
    note = models.CharField(max_length=255)

    def __str__(self):
        return self.form63.patient.user.username


class PolioVaccine(models.Model):
    form63 = models.ForeignKey(Form63, on_delete=models.CASCADE, related_name="polio_vaccines")

    vaccine_type = models.IntegerField(choices=(
        (1, "тОПВ1"),
        (2, "тОПВ2"),
        (3, "тОПВ3"),
        (4, "тОПВ4"),
        (5, "ОПВ дополнительный дозы"),
    ))	 

    date = models.DateField()
    dose = models.FloatField()  
    series = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=255)	
    reaction = models.CharField(max_length=50)
    denial = models.CharField("Медотвод. Дата и причина", max_length=255)
    note = models.CharField(max_length=255)

    def __str__(self):
        return self.form63.patient.user.username


# DiphteriaTetanusPertussisHepatitisBHemophilicInfectionBVaccine
class DTPHHVaccine(models.Model):
    form63 = models.ForeignKey(Form63, on_delete=models.CASCADE, related_name="DTPHH_vaccines") 

    vaccine_type = models.IntegerField(choices=(
        (1, "АКДОЙГВ+ХИ 51"),
        (2, "АКДОВГВ+ХИ Б2"),
        (3, "АКДС+ВГВ+ХИБЗ"),        
    ))

    date = models.DateField()
    dose = models.FloatField()  
    series = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=255)	
    reaction = models.CharField(max_length=50)
    denial = models.CharField("Медотвод. Дата и причина", max_length=255)
    note = models.CharField(max_length=255)	 

    def __str__(self):
        return self.form63.patient.user.username


# Ревакцинация АКДС
class RevactinationAPDTVaccine(models.Model):
    form63 = models.ForeignKey(Form63, on_delete=models.CASCADE, related_name="revactination_APDT_vaccines") 

    vaccine_type = models.IntegerField(choices=(
        (1, "АКДС 2 года"),
        (2, "АДС 6 лет"),
        (3, "АДС-М 11 лет"),
        (3, "АДС-М 16 лет"),
        (3, "АДС-М 26 лет"),
        (3, "АДС-М 36 лет"),
        (3, "АДС-М 46 лет"),
        (3, "АДС-М 56 лет"),        
    ))

    date = models.DateField()
    dose = models.FloatField()  
    series = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=255)	
    reaction = models.CharField(max_length=50)
    denial = models.CharField("Медотвод. Дата и причина", max_length=255)
    note = models.CharField(max_length=255)	 

    def __str__(self):
        return self.form63.patient.user.username


# Против кори, эпитпаротита и краснухи
class MEPRVaccine(models.Model):
    form63 = models.ForeignKey(Form63, on_delete=models.CASCADE, related_name="MEPR_vaccines") 
    
    vaccine_type = models.IntegerField(choices=(
        (1, "КПК"),
        (2, "КК"),
    ))
	 
    age	= models.IntegerField() 
    date = models.DateField()
    dose = models.FloatField()  
    series = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=255)	
    reaction = models.CharField(max_length=50)
    denial = models.CharField("Медотвод. Дата и причина", max_length=255)	

    def __str__(self):
        return self.form63.patient.user.username


class InfectionVaccine(models.Model):
    form63 = models.ForeignKey(Form63, on_delete=models.CASCADE, related_name="infection_vaccines") 
    vaccine_type = models.CharField(max_length=50)
    age	= models.IntegerField() 
    date = models.DateField()
    dose = models.FloatField()  
    series = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=255)	
    reaction = models.CharField(max_length=50)
    denial = models.CharField("Медотвод. Дата и причина", max_length=255)	

    def __str__(self):
        return self.form63.patient.user.username


# Национальные Дни Иммунизации
class NIDVaccine(models.Model):
    form63 = models.ForeignKey(Form63, on_delete=models.CASCADE, related_name="NID_vaccines") 
    vaccine_type = models.CharField(max_length=50)
    age	= models.IntegerField() 
    date = models.DateField()
    dose = models.FloatField()  
    series = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=255)	
    reaction = models.CharField(max_length=50)
    denial = models.CharField("Медотвод. Дата и причина", max_length=255)	

    def __str__(self):
        return self.form63.patient.user.username	

