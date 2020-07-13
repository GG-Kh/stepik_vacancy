from django import forms

from vacancy.models import Company, Application, Vacancy, Resume


class CompanyCreateForm(forms.ModelForm):

    class Meta:
        model = Company

        fields = (
            'name',
            'location',
            'logo',
            'description',
            'employee_count',
        )


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application

        fields = (
            'written_username',
            'written_phone',
            'written_cover_letter',
        )


class VacancyForm(forms.ModelForm):

    class Meta:
        model = Vacancy

        fields = (
            'title',
            'skills',
            'description',
            'salary_min',
            'salary_max',
        )


class ResumeForm(forms.ModelForm):

    status = forms.ChoiceField(
        choices=Resume.STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}))
    specialty = forms.ChoiceField(
        choices=Resume.SPECIALTY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}))
    grade = forms.ChoiceField(
        choices=Resume.GRADE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:

        model = Resume

        fields = (
            'name',
            'surname',
            'status',
            'salary',
            'specialty',
            'grade',
            'education',
            'experience',
            'portfolio')
