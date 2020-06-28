from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50, blank=True, null=True)
    logo = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    employee_count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Specialty(models.Model):
    code = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    picture = models.TextField()

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
