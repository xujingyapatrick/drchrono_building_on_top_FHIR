from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.views.generic import TemplateView
from social_django.models import UserSocialAuth
from django.views.generic.edit import CreateView
import requests
import api_functions
import json
from datetime import datetime
from .models import trackerSystem, Patient
from form import trackerForm
def index(request):
	if request.user.is_authenticated():
		request.user.social_auth.get(provider='onpatient')
		patients = api_functions.get_patient_info(socialObj)
		observations = api_functions.get_observation(socialObj)
		#immunizations = api_functions.get_immunization(socialObj)
		#conditions = api_functions.get_condition(socialObj)
		#allergies = api_functions.get_allergy(socialObj)
		# load all tracker data 
		trackerData = trackerSystem.objects.filter(patient = patients[0]['id']).order_by('-Date').reverse()
		index = 0
		trackerDict = {}
		trackerDict['daily_sbp'] = []
		trackerDict['daily_dbp'] = []
		trackerDict['daily_weight'] = []
		trackerDict['daily_hydrate'] = []
		trackerDict['daily_sleep'] = []
		trackerDict['date'] = []
		for data in trackerData:
			trackerDict['daily_sbp'].append(data.Daily_Systolic_Blood_Pressure)
			trackerDict['daily_dbp'].append(data.Daily_Diastolic_Blood_Pressure)
			trackerDict['daily_weight'].append(data.Daily_Weight)
			trackerDict['daily_hydrate'].append(data.Daily_Hydrate_Volume)
			trackerDict['daily_sleep'].append(data.Daily_Sleep_Time)
			trackerDict['date'].append(datetime.strftime(data.Date, "%Y-%m-%d"))
			index += 1

		return render(request, "index.html", {"patient_id" : patients[0]['id'], "patients_data" : patients, "patient_tracker_data" : json.dumps(trackerDict), "observations" : observations, "index" : (index - 1)})
	else:
		return redirect('/')
class trackingCreate(CreateView):
	model = trackerSystem
	form_class = trackerForm
	#fields = ['patient', 'Daily_Systolic_Blood_Pressure', 'Daily_Diastolic_Blood_Pressure', 'Daily_Weight', 'Daily_Hydrate_Volume', 'Daily_Sleep_Time', 'Date']

	def get_initial(self):
		patient = get_object_or_404(Patient, id = self.kwargs.get('id'))
		print (patient.id)
		return {
			'patient' : patient
		}
	
