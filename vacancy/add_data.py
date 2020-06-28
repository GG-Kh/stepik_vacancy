from datetime import datetime
from os import path, environ
import sys

import data

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
environ['DJANGO_SETTINGS_MODULE'] = 'stepik_vacancy.settings'

import django

django.setup()

from vacancy.models import Company, Specialty, Vacancy


for i in range(len(data.companies)):
    company = Company()
    company.name = data.companies[i].get('title')
    company.logo = f'https://raw.githubusercontent.com/kushedow/flask-html/mast\
        er/Django%20Project%202/static/logo{i+1}.png'
    company.save()


for i in data.specialties:
    specialty = Specialty()
    specialty.code = i.get('code')
    specialty.title = i.get('title')
    specialty.picture = f'https://raw.githubusercontent.com/kushedow/flask-ht\
        ml/master/Django%20Project%202/specialties/specty_{i.get("code")}.png'
    specialty.save()


for i in data.jobs:
    vacancy = Vacancy()
    vacancy.title = i.get('title')
    vacancy.description = i.get('desc')
    vacancy.salary_min = i.get('salary_from')
    vacancy.salary_max = i.get('salary_to')
    date = datetime.strptime(i.get('posted'), '%Y-%m-%d').date()
    vacancy.published_at = date
    vacancy.specialty = Specialty.objects.get(code=i.get('cat'))
    vacancy.company = Company.objects.get(name=i.get('company'))
    vacancy.save()
