# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_registration_app.models import User
from django.db import models

# Create your models here.
class QuotesManager(models.Manager):
	pass
	# def quote_validation(self,postData,sessionData):
	# 	quotes = []
	# 	for quote in Quotes.objects.all():
	# 			in_favorites = False
	# 			for favorite_quote in Favorite_Quotes.objects.filter(user=User.objects.get(id=sessionData['user_id'])):	
	# 				print "QUOTE" + str(quote)
	# 				print favorite_quote.quote
	# 				if quote == favorite_quote.quote:
	# 					print "I found quote in Favorites"
	# 					in_favorites = True
	# 			if not in_favorites:
	# 				print quote
	# 				quotes.append(quote)
	# 	return quotes			
		# Quote.objects.create(name=postData['name'],content=postData['content'],user=User.objects.get(id=postData['user_id']))

class Quotes(models.Model):
	name = models.CharField(max_length=255)
	content = models.CharField(max_length=255)
	user = models.ForeignKey('login_registration_app.User',related_name='created_by')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = QuotesManager()
	def __repr__(self):
		return "<Quotes object: {} {} {}>".format(self.name,self.content,self.id)

class Favorite_Quotes(models.Model):
	user = models.ForeignKey('login_registration_app.User',related_name='favorites_user')
	quote = models.ForeignKey(Quotes,related_name='quotes_favorite')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	
	def __repr__(self):
		return "<Favorite_Quotes object: {} {}>".format(self.user,self.quote)

	objects = QuotesManager()