from django import forms
from .models import JobCategory, EmploymentType, Job
from django.utils.translation import gettext_lazy as _


class JobSearchForm(forms.Form):
    GENDER_CHOICES = [
        ('', 'Both'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    COUNTRY_CHOICES = [
        ('Afghanistan', 'Afghanistan'),
    ]
    EmploymentType = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
    ]
    keyword = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control input-search', 'placeholder': _('Keyword (e.g., Job Title, Organization)')}), required=False)
    category = forms.ModelChoiceField(queryset=JobCategory.objects.all(), empty_label=_('Select Category'), required=False, widget=forms.Select(attrs={'class': 'mr-2 form-control'}))
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, widget=forms.Select(attrs={'class': 'mr-2 form-control', 'placeholder': _('Country')}), required=False)
    province = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'mr-2 form-control', 'placeholder': _('Province/State')}), required=False)
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('City')}), required=False)
    employment_type = forms.ChoiceField(choices=EmploymentType, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'placeholder':_('Gender')}), required=False)

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['trans_languages']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'organization': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'submission_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'employment_type': forms.Select(attrs={'class': 'form-select'}),
            'salary': forms.TextInput(attrs={'class': 'form-control'}),
            'vacancy_number': forms.TextInput(attrs={'class': 'form-control'}),
            'no_of_jobs': forms.NumberInput(attrs={'class': 'form-control'}),
            'organization': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'contract_duration': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'close_date': forms.DateInput(attrs={'class': 'form-control'}),
            'submission_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'language': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'province': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'years_of_experience': forms.TextInput(attrs={'class': 'form-control'}),
            'education': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'submission_guideline': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'created_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'credit': forms.TextInput(attrs={'class': 'form-control'}),
        }