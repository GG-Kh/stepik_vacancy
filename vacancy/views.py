from django.shortcuts import render
from django.views import View
from django.http import Http404, HttpResponse

from vacancy.models import Company, Specialty, Vacancy


class MainView(View):

    def get(self, request):
        company_all = Company.objects.all()
        specialty_all = Specialty.objects.all()

        specialties = []
        companies = []

        for specialty in specialty_all:
            count = Vacancy.objects.filter(specialty=specialty.pk).count()
            specialties.append({
                'code': specialty.code,
                'title': specialty.title,
                'picture': specialty.picture,
                'count': count
                })

        for company in company_all:
            count = Vacancy.objects.filter(company=company.pk).count()
            companies.append({
                'name': company.name,
                'logo': company.logo,
                'count': count,
                'id': company.pk
                })

        context = {
            'specialties': specialties,
            'companies': companies
        }

        return render(request, 'index.html', context=context)


class VacanciesView(View):

    def get(self, request):

        vacancy_all = Vacancy.objects.all()
        vacancies = []

        for vacancy in vacancy_all:
            company = Company.objects.filter(name=vacancy.company).first()

            vacancies.append({
                'vacancy_id': vacancy.pk,
                'title': vacancy.title,
                'salary_min': vacancy.salary_min,
                'salary_max': vacancy.salary_max,
                'published_at': vacancy.published_at,
                'logo': company.logo,
                'company_id': company.pk
            })

        context = {'vacancies': vacancies}
        return render(request, 'vacancies.html', context=context)


class VacanciesCategoryView(View):

    def get(self, request, category):

        specialty = Specialty.objects.filter(code=category).first()

        vacancy_all = Vacancy.objects.filter(specialty=specialty)
        vacancies = []

        for vacancy in vacancy_all:
            company = Company.objects.filter(name=vacancy.company).first()

            vacancies.append({
                'vacancy_id': vacancy.pk,
                'title': vacancy.title,
                'salary_min': vacancy.salary_min,
                'salary_max': vacancy.salary_max,
                'published_at': vacancy.published_at,
                'logo': company.logo,
                'company_id': company.pk
            })

        context = {
            'vacancies': vacancies,
            'specialty': specialty.title
            }

        return render(request, 'vacancies_cat.html', context=context)


class VacancyDetailView(View):

    def get(self, request, id):

        try:
            vacancy = Vacancy.objects.get(pk=id)
            company = Company.objects.filter(name=vacancy.company).first()

            context = {
                'vacancy': vacancy,
                'company': company
            }

            return render(request, 'vacancy.html', context=context)

        except Vacancy.DoesNotExist:
            raise Http404('Такой вакансии нет!')


class CompaniesView(View):

    def get(self, request, id):

        try:
            company = Company.objects.get(pk=id)
            vacancies = Vacancy.objects.filter(company=company.pk)

            context = {
                'company': company,
                'vacancies': vacancies,
                'count': vacancies.count()
            }

            return render(request, 'company.html', context=context)

        except Company.DoesNotExist:
            raise Http404('Такой компании нет!')


def handler404(request, *args, **kwargs):
    return HttpResponse('Страница не найдена!')


def handler500(request, *args, **kwargs):
    return HttpResponse('Что-то пошло не так!')
