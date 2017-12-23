from django import forms
from .models import trackerSystem, Patient
class trackerForm(forms.ModelForm):
	class Meta:
		model = trackerSystem
		fields = ['patient', 'Daily_Systolic_Blood_Pressure', 'Daily_Diastolic_Blood_Pressure', 'Daily_Weight', 'Daily_Hydrate_Volume', 'Daily_Sleep_Time', 'Date']

		widgets = {'patient' : forms.HiddenInput()}