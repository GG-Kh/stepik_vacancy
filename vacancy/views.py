from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.http import HttpResponse
from django.db.models import Count
from django.contrib.auth.models import User

from datetime import datetime

from vacancy.models import Company, Specialty, Vacancy, Application, Resume
from vacancy.forms import CompanyCreateForm, ApplicationForm, VacancyForm
from vacancy.forms import ResumeForm


class MainView(View):

    def get(self, request):

        specialties = Specialty.objects.annotate(count=Count('vacancies'))
        companies = Company.objects.annotate(count=Count('vacancies'))

        context = {
            'specialties': specialties,
            'companies': companies}

        return render(request, 'index.html', context=context)


class VacanciesView(View):

    def get(self, request):

        vacancies = Vacancy.objects.all()
        context = {'vacancies': vacancies}
        return render(request, 'vacancies.html', context=context)


class VacanciesCategoryView(View):

    def get(self, request, category):

        specialty = Specialty.objects.filter(code=category).first()
        vacancies = Vacancy.objects.filter(specialty=specialty)

        context = {
            'vacancies': vacancies,
            'specialty': specialty
            }

        return render(request, 'vacancies_cat.html', context=context)


class VacancyDetailView(View):

    def get(self, request, id):

        form = ApplicationForm

        vacancy = Vacancy.objects.filter(pk=id).first()
        company = Company.objects.filter(name=vacancy.company).first()

        context = {
            'vacancy': vacancy,
            'company': company,
            'form': form}

        return render(request, 'vacancy.html', context=context)


class CompaniesView(View):

    def get(self, request, id):

        company = Company.objects.filter(pk=id).first()
        vacancies = Vacancy.objects.filter(company=company.pk)

        context = {
            'company': company,
            'vacancies': vacancies}

        return render(request, 'company.html', context=context)


class VacanciesSendView(View):

    def post(self, request, id):

        form = ApplicationForm(request.POST)

        if form.is_valid():
            respond = form.save(commit=False)
            respond.user = request.user
            respond.vacancy = Vacancy.objects.filter(
                pk=str(request.path).split('/')[-2]).first()
            respond.save()

        context = {
            'previos_url': request.path.replace('send', '')
        }

        return render(request, 'sent.html', context=context)


class MyCompanyView(View):

    def get(self, request):

        username = User.objects.get(username=request.user)
        company = Company.objects.filter(owner=username)

        if company.count() < 1:

            return render(request, 'company-create.html')

        form = CompanyCreateForm(instance=company.first())
        return render(request, 'company-edit.html', context={'form': form})

    def post(self, request):

        username = User.objects.get(username=request.user)
        company = Company.objects.filter(owner=username)

        form = CompanyCreateForm(request.POST, instance=company.first())
        if form.is_valid():
            company = form.save(commit=False)
            company.owner = request.user
            company.save()

        return redirect(reverse('mycompany'))


class MyCompanyCreateView(View):

    def get(self, request):

        form = CompanyCreateForm
        return render(request, 'company-edit.html', context={'form': form})


class MyCompanyVacancies(View):

    def get(self, request):

        company = Company.objects.filter(owner=request.user).first()
        vacancies = Vacancy.objects.filter(company=company).annotate(
            count=Count('applications'))

        context = {
            'vacancies': vacancies
        }

        return render(request, 'vacancy-list.html', context=context)


class MyCompanyVacancyDetailView(View):

    def get(self, request, id):

        vacancy = Vacancy.objects.filter(pk=id).first()
        specialties = Specialty.objects.all()
        applications = Application.objects.filter(vacancy=vacancy)

        form = VacancyForm(instance=vacancy)

        context = {
            'form': form,
            'specialties': specialties,
            'applications': applications
        }

        return render(request, 'vacancy-edit.html', context=context)

    def post(self, request, id):

        vacancy = Vacancy.objects.filter(pk=id).first()
        form = VacancyForm(request.POST, instance=vacancy)

        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.published_at = datetime.now().date()
            vacancy.specialty = Specialty.objects.get(
                code=request.POST.get('specialty'))
            vacancy.company = Company.objects.filter(
                owner=request.user).first()
            vacancy.save()

        return redirect(reverse('mycompany_vacancies'))


class MyCompanyVacancyCreateView(View):

    def get(self, request):

        specialties = Specialty.objects.all()
        form = VacancyForm

        context = {
            'form': form,
            'specialties': specialties,
        }

        return render(request, 'vacancy-edit.html', context=context)

    def post(self, request):

        form = VacancyForm(request.POST)

        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.published_at = datetime.now().date()
            vacancy.specialty = Specialty.objects.get(
                code=request.POST.get('specialty'))
            vacancy.company = Company.objects.filter(
                owner=request.user).first()
            vacancy.save()

        return redirect(reverse('mycompany_vacancies'))


class MyResumeView(View):

    def get(self, request):

        user = User.objects.get(username=request.user)
        resume = Resume.objects.filter(user=user).first()

        if resume is None:
            return render(request, 'resume-create.html')

        form = ResumeForm(instance=resume)

        return render(request, 'resume-edit.html', context={'form': form})

    def post(self, request):

        user = User.objects.get(username=request.user)
        resume = Resume.objects.filter(user=user).first()

        form = ResumeForm(request.POST, instance=resume)

        if form.is_valid():

            myresume = form.save(commit=False)
            myresume.user = request.user
            myresume.save()

        return redirect(reverse('myresume'))


class MyResumeCreateView(View):

    def get(self, request):

        form = ResumeForm
        return render(request, 'resume-edit.html', context={'form': form})

    def post(self, request):

        form = ResumeForm(request.POST)

        if form.is_valid():

            myresume = form.save(commit=False)
            myresume.user = request.user
            myresume.save()

        return redirect(reverse('myresume'))


def handler404(request, *args, **kwargs):
    return HttpResponse('Страница не найдена!')


def handler500(request, *args, **kwargs):
    return HttpResponse('Что-то пошло не так!')
