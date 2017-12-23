from django.db import models

# Create your models here.
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Patient(models.Model):
	id = models.IntegerField(primary_key=True)
	"""
	gender = models.CharField(max_length=100)
	name =  models.CharField(max_length=100)
	birthDate = models.CharField(max_length=100)
	contacts = models.CharField(max_length=250)
	"""
class trackerSystem(models.Model):

    Daily_Systolic_Blood_Pressure = models.FloatField(null=True)
    Daily_Diastolic_Blood_Pressure = models.FloatField(null=True)
    Daily_Weight = models.FloatField(null=True)
    Daily_Hydrate_Volume = models.FloatField(null=True)
    Daily_Sleep_Time = models.FloatField(null=True)
    Date = models.DateTimeField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)

    def get_absolute_url(self):
        return reverse('tracker_app:index')
        