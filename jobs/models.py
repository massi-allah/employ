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
    # General Job Listings Fields
    job_id = models.AutoField(primary_key=True)
    title = models.CharField(_("Title"), max_length=255)
    employment_type = models.CharField(_("Employment Type"), max_length=50, choices=EmploymentType, default='Full Time', null=True, blank=True)  # Default value set to 'male'
    salary = models.CharField(_("Salary"), max_length=255, null=True, blank=True)
    vacancy_number = models.CharField(_("Vacancy Number"), max_length=255, null=True, blank=True)
    no_of_jobs = models.IntegerField(_("Counts"), null=True, blank=True)
    organization = models.CharField(_("Organization"), max_length=255, null=True, blank=True)
    category = models.ManyToManyField('JobCategory')
    contract_duration = models.CharField(_("Contract Duration"), max_length=255, null=True, blank=True)
    nationality = models.CharField(_("Nationality"), max_length=255, null=True, blank=True)
    gender = models.CharField(_("Gender"), max_length=50, choices=GENDER_CHOICES, default='male', null=True, blank=True)  # Default value set to 'male'
    close_date = models.DateField(_("Close date"), null=True, blank=True)
    submission_email = models.EmailField(_("Submission Email"), null=True, blank=True)
    language = models.CharField(_("Language"), max_length=20, default='English', null=True, blank=True)  # Default value set to 'English'
    # Location details
    location = models.CharField(_("location"), max_length=100, null=True, blank=True)
    years_of_experience = models.CharField(_("Years Of Experience"), max_length=200, default='1 year', null=True, blank=True)  # Default value set to '1 year'
    education = models.CharField(_("Education"), max_length=255, default='Bachelor', null=True, blank=True)  # Default value set to 'Bachelor'
    description = models.TextField(_("Description"), null=True, blank=True)
    about_organization = models.TextField(_("About the Organization"), null=True, blank=True)
    job_requirements = models.TextField(_("Job Requirements"), null=True, blank=True)
    submission_guideline = models.TextField(_("Submission Guideline"), null=True, blank=True)
    created_date = models.DateTimeField(_("Created Date"), default=timezone.now, null=True, blank=True)
    announce_date = models.DateTimeField(_("Announce Date"), default=timezone.now, null=True, blank=True)
    credit = models.CharField(max_length=32, null=True, blank=True)

    # Employ Settings
    # Separating the main job from its translation
    is_main = models.BooleanField(default=True)
    # Refers to original job posting if this is translated version of another job
    translation_of = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='translations',
        on_delete=models.SET_NULL
    )
    translation_language = models.CharField(max_length=10, null=True, blank=True, default="en")


    def __str__(self):
        return self.title


class JobCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)

    # Employ Settings
    # Separating the main category from its translation
    is_main = models.BooleanField(default=True)
    # Refers to original job category if this is translated version of another job category
    translation_of = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='translations',
        on_delete=models.SET_NULL
    )
    translation_language = models.CharField(max_length=10, null=True, blank=True, default="en")


    def __str__(self):
        return self.name

