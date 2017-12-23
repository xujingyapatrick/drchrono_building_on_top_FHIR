# drchrono Project - Building on top of FHIR API
- A Project written in Pyhon/Django + JQuery + Bootstrap + Responsive Web Design
- started with https://github.com/drchrono/api-example-django
- It allows user to login with Onpatient account, to retrieve all information on Onpatient.com
- Other features: Blood Presure Tracker, Hydrate Tracker, Sleep Tracker, Weight Tracker
### Requirements
- [pip](https://pip.pypa.io/en/stable/)
- [python virtual env](https://packaging.python.org/installing/#creating-and-using-virtual-environments)

### Setup
``` bash
$ pip install -r requirements.txt
$ python manage.py runserver
```

`social_auth_drchrono/` contains a custom provider for [Python Social Auth](http://python-social-auth.readthedocs.io/en/latest/) that handles OAUTH for drchrono. To configure it, set these fields in your `drchrono/settings.py` file:

```
SOCIAL_AUTH_DRCHRONO_KEY
SOCIAL_AUTH_DRCHRONO_SECRET
LOGIN_REDIRECT_URL
```

# Design Decision
## Information from Onpatient.com
- Except for patient information, also retrieve the last recoreded vital sign from doctor. 
- The reason is that, from patients' perpective, paitents should be care of the last recorded information by visiting the doctor
## Database
- Once patients login successfully, only stored their Patient ID to database, this Patient ID will be associated with Tracker Systems later
## Statistic Visualization 
- Using highcharts.js to display data in a visual way, which is the best way for patients to see all changes 

## Screenshot for Login Page
![login_pag](https://user-images.githubusercontent.com/18036551/34318657-4f2955c4-e783-11e7-9799-8159fecb2b61.png)

## Screenshot for Patient Information
![personal_info](https://user-images.githubusercontent.com/18036551/34318659-65b5cc1e-e783-11e7-87d4-42a83c76e15d.png)

![recorded_info](https://user-images.githubusercontent.com/18036551/34318663-6c1bc2c0-e783-11e7-94a2-ebdbcc46f563.png)

## Screenshot for Adding Data to Tracker System
![adding_data](https://user-images.githubusercontent.com/18036551/34318667-77782c44-e783-11e7-8cab-5d6ade91f4c7.png)

## Screenshot for Tracker System
![blood_pressure_tracker](https://user-images.githubusercontent.com/18036551/34318670-7f86902e-e783-11e7-85a4-bb5d1be61621.png)

![weight_tracker](https://user-images.githubusercontent.com/18036551/34318671-83a7fd96-e783-11e7-8e15-83c1a566eb3d.png)
