# Create your views here.
# -*- coding: utf8 -*-
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from v_site.models import Academys, Subjects, Teachers, Courses, Students


def home_handler(request, template_name):
	return render(request, template_name, {'user_id': request.user.id})

@login_required
def personal_handler(request, template_name):
	student = Students.objects.get(stu_id=request.user.username)
	course = student.stu_course.all()
	if student:
		return render_to_response(template_name,{'student':student, 'course':course, 'user_id':request.user.id})

def about_handler(request, template_name):
	return render(request, template_name, {'user_id': request.user.id})

@csrf_exempt
def request_login_handler(request, template_name):#login.html
	if request.user.is_authenticated():
		return HttpResponseRedirect('/personal/')
	
	next = request.GET.get('next','')
	login_error = False
	if request.method == 'POST':
		next = request.POST.get('next','')
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		
		if user is None:
			login_error = True
		#login success
		if user is not None and user.is_active:
			auth.login(request, user)
			if next:
				return HttpResponseRedirect(next)
			else:
				return HttpResponseRedirect('/')
	
	return render_to_response(template_name,{'next':next,'login_error':login_error},context_instance=RequestContext(request))

def request_logout_handler(request, template_name):
	auth.logout(request)
	return HttpResponseRedirect('/')

def check_course_handler(request, template_name):

	return render(request, template_name, {'user_id': request.user.id})

def teacher_handler(request, template_name):
	return render(request, template_name)

def teacherpersonal_handler(request, template_name):
	return render(request, template_name)

def homeworkre_handler(request, template_name):
	return render(request, template_name)

def teacherco_handler(request, template_name):
	return render(request, template_name)