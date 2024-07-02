from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
EmploymentType = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
    ]
class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    title = models.CharField(_("Title"), max_length=255)
    employment_type = models.CharField(_("Employment Type"), max_length=50, choices=EmploymentType, default='Full Time')  # Default value set to 'male'
    salary = models.CharField(_("Salary"), max_length=255)
    vacancy_number = models.CharField(_("Vacancy Number"), max_length=255)
    no_of_jobs = models.IntegerField(_("Counts"))
    organization = models.CharField(_("Organization"), max_length=255)
    category = models.ForeignKey('JobCategory', on_delete=models.CASCADE)
    contract_duration = models.CharField(_("Contract Duration"), max_length=255)
    gender = models.CharField(_("Gender"), max_length=50, choices=GENDER_CHOICES, default='male')  # Default value set to 'male'
    close_date = models.DateField(_("Close date"))
    submission_email = models.EmailField(_("Submission Email"), null=True)
    language = models.CharField(_("Language"), max_length=20, default='English', null=True, blank=True)  # Default value set to 'English'

    # Translation fields
    trans_languages = models.JSONField(default=dict, null=True, blank=True)

    # Location details
    country = models.CharField(_("Country"), max_length=100, default='Afghanistan')  # Default value set to 'Afghanistan'
    province = models.CharField(_("Province"), max_length=100, blank=True, null=True)
    city = models.CharField(_("City"), max_length=100, null=True, blank=True)

    years_of_experience = models.CharField(_("Years Of Experience"), max_length=200, default='1 year')  # Default value set to '1 year'
    education = models.CharField(_("Education"), max_length=255, default='Bachelor')  # Default value set to 'Bachelor'

    description = models.TextField(_("Description"))
    submission_guideline = models.TextField(_("Submission Guideline"))

    created_date = models.DateTimeField(_("Created Date"), default=timezone.now)
    credit = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.title


class JobCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)

    # Translation  fields
    trans_languages = models.JSONField(default=dict, null=True, blank=True)


    def __str__(self):
        return self.name

