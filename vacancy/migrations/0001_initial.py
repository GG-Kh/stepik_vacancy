# Generated by Django 3.0.7 on 2020-07-10 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(
                    blank=True, max_length=50, null=True)),
                ('logo', models.ImageField(upload_to='company_images')),
                ('description', models.TextField(blank=True, null=True)),
                ('employee_count', models.IntegerField(blank=True, null=True)),
                ('owner', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='speciality_images')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('skills', models.TextField(blank=True, null=True)),
                ('description', models.TextField()),
                ('salary_min', models.IntegerField()),
                ('salary_max', models.IntegerField()),
                ('published_at', models.DateField()),
                ('company', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='vacancies', to='vacancy.Company')),
                ('specialty', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='vacancies', to='vacancy.Specialty')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('written_username', models.CharField(max_length=30)),
                ('written_phone', models.CharField(max_length=30)),
                ('written_cover_letter', models.TextField()),
                ('company', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='applications', to=settings.AUTH_USER_MODEL)),
                ('vacancy', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='applications', to='vacancy.Vacancy')),
            ],
        ),
    ]
