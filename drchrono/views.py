from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from social_django.models import UserSocialAuth
import requests
from django.contrib.auth import logout

def logout_view(request):
	logout(request)
	return render(request, 'login.html')