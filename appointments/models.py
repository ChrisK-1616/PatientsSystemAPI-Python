# File: models.py
# Description: Autogenerated file from the "django-admin startapp" facility - modified for the specific
#              application "panda/appointments"
# Author: Chris Knowles
# Date: Jun 2023


from django.db import models


# Create your models here.
class Department(models.Model):
    """
    :summary: Model for departments which are associated with appointments, a department
    may be allocated to many appointments but only one department is associated with any
    given appointment - note the name of the department is used as its key

    :property name: full name of the department persisted as an UTF8 string of up to 200
                    characters, note - this can be stored as unicode characters to allow
                    for non-latin character sets
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        """
        :summary: Provides a JSON string for the Department model instance

        :return: JSON string as string
        """
        return f'''{{"name": "{self.name}"}}'''


class Clinician(models.Model):
    """
    :summary: Model for clinicians which are associated with appointments, a clinician may
    be allocated to many appointments but only one clinician is associated with any given
    appointment - note the name of the clinician is used as its key

    :property name: full name of the clinician persisted as an UTF8 string of up to 200
                    characters, note - this can be stored as unicode characters to allow
                    for non-latin character sets
    """
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        """
        :summary: Provides a JSON string for the Clinician model instance

        :return: JSON string as string
        """
        return f'''{{"name": "{self.name}", "department": "{self.department.name}"}}'''


class Patient(models.Model):
    """
    :summary: Model for patients which are associated with appointments, a patient may have
    many appointments but only one patient is associated with any given appointment

    :property nhs_number:    unique identifier for the patient within all NHS systems, it is
                             persisted as a string of exactly 10 digit characters and must
                             be validated against the NHS number checksum algorithm before
                             being accepted and stored
    :property name:          full name of the patient persisted as an UTF8 string of up to 200
                             characters, note - this can be stored as unicode characters to
                             allow for non-latin character sets
    :property date_of_birth: full year, month and day of the patient's birthdate persisted as
                             date type data
    :property postcode:      home address postcode of the patient persisted as a string of up
                             to 8 characters in the coerced form with a space character between
                             the Outward code and the Inward code
    """
    nhs_number = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    postcode = models.CharField(max_length=8)

    def __str__(self):
        """
        :summary: Provides a JSON string for the Patient model instance

        :return: JSON string as string
        """
        return f'''
                {{"nhs_number": "{self.nhs_number}", "name": "{self.name}",
                "date_of_birth": "{self.date_of_birth}", "postcode": "{self.postcode}"}}
                '''


class Appointment(models.Model):
    """
    :summary: Model for appointments which are associated with patients at a given date and
    time, for a given duration and with a given clinician from their specific department, a
    single patient may have many appointments but only one patient and one clinician is
    associated with any given appointment - note that an appointment instance is uniquely
    identified by a combination of both the patient NHS number and the datetime of the
    appointment, this is because an appointment may only have one patient associated with
    it and that patient can only be associated with one appointment at any given datetime

    :property patient:    reference to the NHS number of the patient persisted as a foreign
                          key into the Patient models
    :property status:     an indicator of the status of the appointment which will be of the
                          value "active", "attended", "missed" or "cancelled", persisted as
                          a string of the corresponding to a value taken from the previous
                          list of valid values so requires up to 9 characters
    :property time:       full year, month, day, hours and minutes of the appointment's date
                          and time persisted as string of up to 25 characters
    :property duration:   duration in hours and minutes the appointment is estimated to last
                          persisted as string of up to 16 characters
    :property clinician:  reference to the clinician that the appointment is with persisted
                          as a foreign key into the Clinician models
    :property department: reference to the department that the appointment is within persisted
                          as a foreign key into the Department models
    :property uuid:       UUID style unique identifier for the appointment persisted as a
                          string of exactly 36 characters
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    status = models.CharField(max_length=9)
    time = models.CharField(max_length=25)
    duration = models.CharField(max_length=16)
    clinician = models.ForeignKey(Clinician, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=36)

    def __str__(self):
        """
        :summary: Provides a JSON string for the Appointment model instance

        :return: JSON string as string
        """
        return f'''
                {{"patient": "{self.patient.nhs_number}", "status": "{self.status}",
                "time": "{self.time}", "duration": "{self.duration}",
                "clinician": "{self.clinician.name}",
                "department": "{self.department.name}",
                "postcode": "{self.patient.postcode}", "id": "{self.uuid}"}}
                '''
