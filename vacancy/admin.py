from django.contrib import admin

from vacancy.models import Vacancy, Application, Specialty, Company, Resume

admin.site.register(Vacancy)
admin.site.register(Application)
admin.site.register(Specialty)
admin.site.register(Company)
admin.site.register(Resume)
