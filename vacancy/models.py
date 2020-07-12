from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Company(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50, blank=True, null=True)
    logo = models.ImageField(
        upload_to=settings.MEDIA_COMPANY_IMAGE_DIR,
        blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    employee_count = models.IntegerField(blank=True, null=True)
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Specialty(models.Model):
    code = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    picture = models.ImageField(upload_to=settings.MEDIA_SPECIALITY_IMAGE_DIR)

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField(max_length=50)
    skills = models.TextField(blank=True, null=True)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()
    specialty = models.ForeignKey(
        Specialty,
        on_delete=models.CASCADE,
        related_name="vacancies")
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="vacancies")

    def __str__(self):
        return self.title


class Application(models.Model):
    written_username = models.CharField(max_length=30)
    written_phone = models.CharField(max_length=30)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.CASCADE,
        related_name="applications")
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="applications")

    def __str__(self):
        return self.written_username


class Resume(models.Model):

    STATUS_CHOICES = (
        ('1', 'Ищу работу'),
        ('2', 'Рассматриваю предложения'),
        ('3', 'Не ищу работу')
    )

    SPECIALTY_CHOICES = (
        ('backend', 'Бэкенд'),
        ('frontend', 'Фронтенд'),
        ('gamedev', 'Геймдев'),
        ('devops', 'Девопс'),
        ('design', 'Дизайн'),
        ('products', 'Продукты'),
        ('management', 'Менеджмент'),
        ('testing', 'Тестирование'),
    )

    GRADE_CHOICES = (
        ('trainee', 'Стажер'),
        ('junior', 'Джуниор'),
        ('middle', 'Миддл'),
        ('senior', 'Синьор'),
        ('lead', 'Лид'),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    salary = models.IntegerField()
    specialty = models.CharField(max_length=30, choices=SPECIALTY_CHOICES)
    grade = models.CharField(max_length=30, choices=GRADE_CHOICES)
    education = models.TextField()
    experience = models.CharField(max_length=15)
    portfolio = models.TextField()

    def __str__(self):
        return f'{self.name} {self.surname}'
