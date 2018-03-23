# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_registration_app.models import User
from models import *
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	if 'user_id' not in request.session:
		return redirect('/main')

	return render(request,'quotes_app/index.html',{'user_name':User.objects.filter(id=request.session['user_id'])[0].name})

def show(request,user_id):
	if 'user_id' not in request.session:
		return redirect('/main')
	user = User.objects.get(id=user_id)
		
	context = {
		'user_name':user.name,
		'count':len(Quotes.objects.filter(user=user)),
		'quotes':Quotes.objects.filter(user=user),

	}

	return render(request,'quotes_app/show.html',context)

def show_quotes(request):
	if 'user_id' not in request.session:
		return redirect('/main')
	
	# quotes = Quotes.objects.quote_validation(request.POST,request.session)
	quotes = []
	for quote in Quotes.objects.all():
		print request.session['user_id']
		in_favorites = False
		for favorite_quote in Favorite_Quotes.objects.filter(user=User.objects.get(id=request.session['user_id'])):	
			print "QUOTE" + str(quote)
			print favorite_quote.quote
			if quote == favorite_quote.quote:
				print "I found quote in Favorites"
				in_favorites = True
		if not in_favorites:
			print quote
			quotes.append(quote)
	context = {
		'user_name':User.objects.get(id=request.session['user_id']).name,
		'favorite_quotes': Favorite_Quotes.objects.filter(user=User.objects.get(id=request.session['user_id'])),
		'quotes': quotes

	}

	return render(request,'quotes_app/quotes.html',context)			
def new_quote(request):
	if 'user_id' not in request.session:
		return redirect('/main')

	print "I'm in new_quote!"	
	created_by = User.objects.get(id=request.session['user_id'])

	Quotes.objects.create(name=request.POST['name'],content=request.POST['content'],user=created_by)
	path = 'users/'+ str(request.session['user_id'])
	return redirect(path)

def add_favorite(request,quote_id):
	if 'user_id' not in request.session:
		return redirect('/main')
	Favorite_Quotes.objects.create(user=User.objects.get(id=request.session['user_id']),quote=Quotes.objects.get(id=quote_id))
	return redirect('/quotes')

def delete_favorite(request,quote_id):
	if 'user_id' not in request.session:
		return redirect('/main')
	# user = User.objects.get(id=request.session['user_id'])
	# quote = Quotes.objects.get(id=quote_id)	
	# print quote.id
	# print "user id" + str(user.id)
	# print "user"+str(user)
	quote_delete = Favorite_Quotes.objects.get(id=quote_id)
	print quote_delete
	quote_delete.delete()
	return redirect('/quotes')			