# drchrono Project - Building on top of FHIR API
- A Project written in Pyhon/Django + Highcharts Javascript + JQuery + Bootstrap
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
SOCIAL_AUTH_DRCHRONO_SCOPE
LOGIN_REDIRECT_URL
```

# Design Decision
## Database
Once user login successfully, only stored their Patient ID to database, this Patient ID will be associated with Tracker Systems later
