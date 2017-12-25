from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.views.generic import TemplateView
from social_django.models import UserSocialAuth
from django.views.generic.edit import CreateView
import requests
import api_functions
import json
from .models import trackerSystem, Patient
from form import trackerForm
def index(request):
	if request.user.is_authenticated():
		socialObj = request.user.social_auth.get(provider='onpatient')
		patients = api_functions.get_patient_info(socialObj)
		observations = api_functions.get_observation(socialObj)
		#immunizations = api_functions.get_immunization(socialObj)
		#conditions = api_functions.get_condition(socialObj)
		#allergies = api_functions.get_allergy(socialObj)
		# load all tracker data 
		request.session['user_id'] = patients[0]['id']
		trackerDict = api_functions.get_trackerSystem(patients[0]['id'])
		
		return render(request, "index.html", {"patients_data" : patients, "patient_tracker_data" : json.dumps(trackerDict), "observations" : observations})
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
	
