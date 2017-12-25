import requests
from models import Patient, trackerSystem
from datetime import datetime

def get_immunization(social):
    headers = {'Authorization': 'Bearer %s' % social.extra_data['access_token']}
    immunizations = []
    url = 'https://drchrono.com/onpatient_api/fhir/Immunization'
    
    while url:
        data = requests.get(url, headers=headers).json()
        immunizations.extend(data['results'])
        url = data['next']
        
    return immunizations
def get_condition(social):
    headers = {'Authorization': 'Bearer %s' % social.extra_data['access_token']}
    conditions = []
    url = 'https://drchrono.com/onpatient_api/fhir/Condition'
    
    while url:
        data = requests.get(url, headers=headers).json()
        conditions.extend(data['results'])
        url = data['next']
        
    return conditions
def get_allergy(social):
    headers = {'Authorization': 'Bearer %s' % social.extra_data['access_token']}
    allergies = []
    url = 'https://drchrono.com/onpatient_api/fhir/AllergyIntolerance'
    
    while url:
        data = requests.get(url, headers=headers).json()
        allergies.extend(data['results'])
        url = data['next']
        
    return allergies
def get_patient_info(social):
    headers = {'Authorization': 'Bearer %s' % social.extra_data['access_token']}
    patients = []
    url = 'https://drchrono.com/onpatient_api/fhir/Patient'    
    data = requests.get(url, headers=headers).json()
    patients.extend(data['results'])    
    patients_data = []
    for patient in patients:
        contacts = []
        for contact in patient['telecom']:
            contacts.append(contact['use'] + " " + contact['system'] + " : " + contact['value'])
        person = {
            "id" : patient['identifier'], 
            "name" : patient['name'][0]['given'][0] + " " + patient['name'][0]['family'][0], 
            "gender" : patient['gender'], 
            "birthDate" : patient['birthDate'],
            "contacts" : contacts
        }
        if not Patient.objects.filter(id = person['id']).exists():
            patient_obj = Patient.objects.create(
                id = person['id'],
            )
            patient_obj.save()
        patients_data.append(person)  
        
    return patients_data
    
def get_observation(social):
    headers = {'Authorization': 'Bearer %s' % social.extra_data['access_token']}
    observations = []
    url = 'https://drchrono.com/onpatient_api/fhir/Observation'
    
    while url:
        data = requests.get(url, headers=headers).json()
        observations.extend(data['results'])
        url = data['next']

    observDict = {}
    observDict['Systolic_blood_pressure'] = []
    observDict['Diastolic_blood_pressure'] = []
    observDict['Body_height'] = []
    observDict['BMI'] = []
    observDict['Body_weight'] = []
    observDict['Heart_rate'] = []
    observDict['Respiratory_Rate'] = []
    observDict['Oxygen_saturation'] = []
    observDict['timeStamp'] = []
    observDict['Body_tempurature'] = []
    
    for observation in observations:
        if observation['code']['text'] == 'Systolic blood pressure':
            observDict['Systolic_blood_pressure'].append(observation['valueQuantity']['value'])
            ts = split_timestamp(observation['effectiveDateTime'])
            observDict['timeStamp'].append(ts)

        elif observation['code']['text'] == 'Diastolic blood pressure':
            observDict['Diastolic_blood_pressure'].append(observation['valueQuantity']['value'])

        elif observation['code']['text'] == 'Body weight':
            observDict['Body_weight'].append(observation['valueQuantity']['value'])

        elif observation['code']['text'] == 'Body height':
            observDict['Body_height'].append(observation['valueQuantity']['value'])

        elif observation['code']['text'] == 'Heart rate':
            observDict['Heart_rate'].append(observation['valueQuantity']['value'])

        elif observation['code']['text'] == 'Body mass index':
            observDict['BMI'].append(observation['valueQuantity']['value'])

        elif observation['code']['text'] == 'Respiratory Rate':
            observDict['Respiratory_Rate'].append(observation['valueQuantity']['value'])

        elif observation['code']['text'] == 'Oxygen saturation':
            observDict['Oxygen_saturation'].append(observation['valueQuantity']['value'])

        elif observation['code']['text'] == 'Body tempurature':
            observDict['Body_tempurature'].append(observation['valueQuantity']['value'])
    
    return observDict
    
def split_timestamp(timestamp):

    return ' '.join(timestamp.split('T'))

def get_trackerSystem(patient):
    trackerData = trackerSystem.objects.filter(patient = patient).order_by('-Date').reverse() 
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
    return trackerDict
