# File: admin.py
# Description: Autogenerated file from the "django-admin startapp" facility - modified for the specific
#              project "panda"
# Author: Chris Knowles
# Date: Jun 2023


from django.contrib import admin
from .models import Department, Clinician, Patient, Appointment

# Register your models here.
# su: chris em: chris.knowles@btinternet.com pw: P@zzw0rd
admin.site.register(Department)
admin.site.register(Clinician)
admin.site.register(Patient)
admin.site.register(Appointment)
