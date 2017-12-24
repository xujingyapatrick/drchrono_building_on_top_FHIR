import os
from social.backends.oauth import BaseOAuth2


class drchronoOAuth2(BaseOAuth2):
    """
    drchrono OAuth authentication backend
    """

    #name = 'drchrono'
    name = 'onpatient'
    #AUTHORIZATION_URL = 'https://drchrono.com/o/authorize/'
    #ACCESS_TOKEN_URL = 'https://drchrono.com/o/token/'
    AUTHORIZATION_URL = 'https://onpatient.com/o/authorize/'
    ACCESS_TOKEN_URL = 'https://onpatient.com/o/token/'
    ACCESS_TOKEN_METHOD = 'POST'
    REDIRECT_STATE = False
    #USER_DATA_URL = 'https://drchrono.com/api/users/current'
    USER_DATA_URL = 'https://drchrono.com//onpatient_api/fhir/Patient'
    EXTRA_DATA = [
        ('refresh_token', 'refresh_token'),
        ('expires_in', 'expires_in')
    ]
    # TODO: setup proper token refreshing

    def get_user_details(self, response):
        """
        Return user details from drchrono account
        """
        return {'username': response.get('username'),}

    def user_data(self, access_token, *args, **kwargs):
        """
        Load user data from the service
        """
        return self.get_json(
            self.USER_DATA_URL,
            headers=self.get_auth_header(access_token)
        )

    def get_auth_header(self, access_token):
        return {'Authorization': 'Bearer {0}'.format(access_token)}
    
    def get_user_id(self, details, response):
        return response.get('results')[0].get('identifier')
