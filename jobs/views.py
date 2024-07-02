from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.utils.translation import get_language
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Job, JobCategory, EmploymentType
from .forms import JobSearchForm, JobForm
from jdatetime import date


def gregorian_to_jalali(gregorian_date):
    # Convert Gregorian date to Jalali date
    jalali_date = date.fromgregorian(date=gregorian_date)
    return jalali_date

def translateJobModel(job_model):
    # Get the selected language 
        language_code = get_language()
        tranlations = job_model.trans_languages
        # loading models translations
        if language_code in tranlations:
            item_translations = tranlations[language_code]

        # Iterate over keys in item_translations and update attributes of item
            for translation_key, translated_value in item_translations.items():
                setattr(job_model, translation_key, translated_value)


        close_date = job_model.close_date
        created_date = job_model.created_date
        # Convert dates to Jalali format if the language is Persian or Pashto
        if language_code in ['fa', 'ps']:  # 'fa' for Persian, 'ps' for Pashto
            # Convert close date to Jalali
            close_date = job_model.close_date
            job_model.close_date = gregorian_to_jalali(close_date)

            # Convert created date to Jalali
            created_date = job_model.created_date
            job_model.created_date = gregorian_to_jalali(created_date)

        return job_model

def mainpage(request):
    job_listings = Job.objects.all().order_by('-created_date')
    categories = JobCategory.objects.all()

    # Handle form submission and filtering
    if request.method == 'GET':
        form = JobSearchForm(request.GET)
        if form.is_valid():
            keyword = form.cleaned_data.get('keyword')
            category = form.cleaned_data.get('category')
            country = form.cleaned_data.get('country')
            province = form.cleaned_data.get('province')
            city = form.cleaned_data.get('city')
            employment_type = form.cleaned_data.get('employment_type')
            gender = form.cleaned_data.get('gender')

            # Apply filters dynamically
            if keyword:
                job_listings = job_listings.filter(
                    Q(title__icontains=keyword) |
                    Q(description__icontains=keyword))
                    # Q(organization__name__icontains=keyword)) Due to the model and app for managing organizations is turned down until the next update
            if category:
                job_listings = job_listings.filter(category__name__icontains=category)
            if employment_type:
                job_listings = job_listings.filter(employment_type__icontains=employment_type)
            if gender:
                job_listings = job_listings.filter(gender=gender)
            if country:
                job_listings = job_listings.filter(country__icontains=country)
            if province:
                job_listings = job_listings.filter(city__icontains=province)
            if city:
                job_listings = job_listings.filter(city__icontains=city)

    else:
        form = JobSearchForm()

    # Translate job listings
    for job in job_listings:
        translateJobModel(job)

    # Paginate job listings
    paginator = Paginator(job_listings, 21)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs': page_obj,
        'categories': categories,
        'form': form,
    }

    return render(request, 'jobs/main_page.html', context)


def job(request, id):
    item = Job.objects.get(job_id=id)
    translateJobModel(item)
    return render(request, 'jobs/job_detail_page.html', {'job': item})
