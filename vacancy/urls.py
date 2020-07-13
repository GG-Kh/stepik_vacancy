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
    path(
        'vacancies/<int:id>/send',
        views.VacanciesSendView.as_view(),
        name='send'),
    path(
        'mycompany/',
        views.MyCompanyView.as_view(),
        name='mycompany'),
    path(
        'mycompany_create/',
        views.MyCompanyCreateView.as_view(),
        name='mycompany_create'),
    path(
        'mycompany/vacancies/',
        views.MyCompanyVacancies.as_view(),
        name='mycompany_vacancies'),
    path(
        'mycompany/vacancies/<int:id>/',
        views.MyCompanyVacancyDetailView.as_view(),
        name='mycompany_vacancy_detail'),

    path(
        'mycompany_vacancy_create',
        views.MyCompanyVacancyCreateView.as_view(),
        name='mycompany_vacancy_create'),
    path(
        'myresume/',
        views.MyResumeView.as_view(),
        name='myresume'),
    path(
        'myresume_create/',
        views.MyResumeCreateView.as_view(),
        name='myresume_create'),
    path(
        'search/',
        views.SearchView.as_view(),
        name='search')
    ]
