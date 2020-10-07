from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
from allauth.socialaccount import providers
from allauth.socialaccount.models import SocialLogin, SocialToken, SocialApp
from allauth.socialaccount.providers.facebook.views import fb_complete_login
from allauth.socialaccount.helpers import complete_social_login
import json
from reddit_posts import views

def view_name(request):
	return render(request , 'tempi.html')
    # return HttpResponse('<H1> abcdcskj eks </H1> jgaefhk  <p> sxnsgajfis nhiudhskj gkgshkjfes </p>')

def home(request):
	# return render(request, template_name)
	token = SocialToken.objects.get(account__user=request.user, account__provider='reddit')
	# token = request.GET['code']
	username = ""
	if request.user.is_authenticated:
		username = request.user.username
	us1 = get_username(token)
	return HttpResponse('<H1> abcdcskj eks ' + str(username) + "   " + str(us1) + '</H1> jgaefhk  <p> sxnsgajfis nhiudhskj gkgshkjfes </p>')

def user_agent():
	return "temp_name"

def base_headers():
    return {"User-Agent": user_agent()}

def get_username(access_token):
	print(access_token)
	headers = base_headers()
	headers.update({"Authorization": "bearer " + str(access_token)})
	response = requests.get("https://oauth.reddit.com/subreddits/mine/subscriber.json", headers=headers)
	me_json = response.json()
	# print(me_json)
	for i in range (len(me_json['data']['children'])):
		views.call_posts(me_json['data']['children'][i]['data']['display_name_prefixed'] , headers)
	return me_json['data']['children'][0]['data']['display_name_prefixed']

