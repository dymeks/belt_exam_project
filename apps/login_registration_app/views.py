# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import bcrypt
# from ..book_review_app.models import Book,Review,Author
from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages
# Create your views here.
def index(request):
	if 'user_id' in request.session:
		return redirect('/quotes')
	else:
		return render(request,'login_registration_app/index.html')

def register(request):
	if 'user_id' not in request.session:
		redirect('/')
	response = User.objects.register_validation(request.POST)
	print response
	if not response['status']:
		print response['errors']
		print "There were errors registering"
		for tag, error in response['errors'].iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')	
		# return render(request,'login_registration_app/index.html',context)
	else:
		print "Success!"
		request.session['user_id'] = response['user_id']
		return redirect('/quotes')	
	
	return redirect('/')

def login(request):
	if 'user_id' not in request.session:
		redirect('/')
	print "I'm in the login method"
	response = User.objects.login_validation(request.POST)
	if response['status']:
		print "I am a valid user :( "
		request.session['user_id'] = response['user_id']
		return redirect('/quotes')
	else:
		for tag, error in response['errors'].iteritems():
			messages.error(request, error, extra_tags=tag)
		return redirect('/')
			

def show(request):
	pass

def logout(request):
	request.session.clear()
	return redirect('/main')			