from django.db import models

# Create your models here.

max_length = 255

# 1. Специальности (specialis)
class Specialis(models.Model):
    name = models.CharField(max_length=255, verbose_name='Специальность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'


# 2. Врачи (vrachi) — с фото №1
class Vrachi(models.Model):
    fio = models.CharField(max_length=255, verbose_name='ФИО врача')
    specialis = models.ForeignKey(Specialis, on_delete=models.PROTECT, verbose_name='Специальность')
    start_date = models.DateField(null=True, blank=True, verbose_name='Дата начала работы')
    photo = models.ImageField(upload_to='doctors/%Y/%m/%d/', null=True, blank=True, verbose_name='Фото врача')

    def __str__(self):
        return f"{self.fio} ({self.specialis.name})"

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'


# 3. Больницы (hospital) — с фото №2
class Hospital(models.Model):
    name_org = models.CharField(max_length=200, verbose_name='Название больницы')
    addres = models.TextField(verbose_name='Адрес')
    telephone = models.CharField(max_length=50, verbose_name='Телефон')
    vrach = models.ForeignKey(Vrachi, on_delete=models.PROTECT, verbose_name='Главный врач')
    photo = models.ImageField(upload_to='hospitals/%Y/%m/%d/', null=True, blank=True, verbose_name='Фото здания')

    def __str__(self):
        return self.name_org

    class Meta:
        verbose_name = 'Больница'
        verbose_name_plural = 'Больницы'


# 4. Поликлиники (polyklinika)
class Polyklinika(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название поликлиники')
    addres = models.TextField(null=True, blank=True, verbose_name='Адрес')
    telephone = models.CharField(max_length=50, null=True, blank=True, verbose_name='Телефон')
    vrach = models.ForeignKey(Vrachi, on_delete=models.PROTECT, verbose_name='Заведующий врач')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поликлиника'
        verbose_name_plural = 'Поликлиники'


# 5. Пациенты (patient)
class Patient(models.Model):
    GENDER_CHOICES = [('М', 'Мужской'), ('Ж', 'Женский')]
    fio = models.CharField(max_length=255, verbose_name='ФИО пациента')
    pol = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True, verbose_name='Пол')
    data_rozh = models.DateField(null=True, blank=True, verbose_name='Дата рождения')

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'


# 6. Диагнозы (diagnozu)
class Diagnozu(models.Model):
    diagnoz = models.CharField(max_length=255, verbose_name='Наименование диагноза')

    def __str__(self):
        return self.diagnoz

    class Meta:
        verbose_name = 'Диагноз'
        verbose_name_plural = 'Диагнозы'


# 7. Посещения поликлиники (posehenie_polik)
class PoseheniePolik(models.Model):
    data_posesheniya = models.DateField(verbose_name='Дата посещения')
    time = models.TimeField(null=True, blank=True, verbose_name='Время приёма')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Пациент')
    polyklinika = models.ForeignKey(Polyklinika, on_delete=models.CASCADE, verbose_name='Поликлиника')

    def __str__(self):
        return f"{self.patient.fio} — {self.data_posesheniya}"

    class Meta:
        verbose_name = 'Посещение поликлиники'
        verbose_name_plural = 'Посещения поликлиники'


# 8. Виды операций (vidu_operacuu)
class ViduOperacuu(models.Model):
    name = models.CharField(max_length=255, verbose_name='Вид операции')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид операции'
        verbose_name_plural = 'Виды операций'    