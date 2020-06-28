from django.urls import path

from vacancy import views

urlpatterns = [
    path(
        'vacancies/',
        views.VacanciesView.as_view(),
        name='vacancies'),
    path(
        'vacancies/cat/<str:category>/',
        views.VacanciesCategoryView.as_view(),
        name='vacancies_category'),
    path(
        'vacancies/<int:id>/',
        views.VacancyDetailView.as_view(),
        name='vacancy_detail'),
    path(
        'companies/<int:id>/',
        views.CompaniesView.as_view(),
        name='companies'),
    ]
