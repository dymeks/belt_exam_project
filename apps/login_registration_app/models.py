# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import bcrypt
from django.db import models
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class Rest_UserManager(models.Manager):
	def register_validation(self,postData):
		errors = {}
		result = {
			'status':False
		}

		if(len(postData['name']) < 2 or len(postData['alias']) < 2):
			errors['name_length'] = "Name must be at least 2 letters long."
		elif(not str(postData['name']).isalpha() or not str(postData['alias']).isalpha()):
			errors['name_letters'] = "Names must be all letters and contain no numbers or special characters"
		
		if(len(postData['password']) <= 8 or (postData['password'] != postData['password_confirm'])):
			errors['password'] = "Password must be at least 8 characters and password and password_confirm must match!"
		
		isValidEmail = EMAIL_REGEX.match(postData['email'])
	
		if(len(postData['email']) == 0):
			print "NEED EMAIL"
			errors['email_length'] = "Must submit an Email!"
		if(not isValidEmail):
			print "EMAIL NOT VALID"
			errors['valid_email'] = "Invalid email!"
		print "ERRORS: " + str(errors)	
		if not bool(errors):
			hashed_password = bcrypt.hashpw(postData['password'].encode(),bcrypt.gensalt()) 
			print "Hashed: " + hashed_password
			verify_unique_email = User.objects.filter(email=postData['email'])
			if(len(verify_unique_email) == 0):
				print "I am added to the database!"
				new_user = User.objects.create(name=postData['name'],alias=postData['alias'],email=postData['email'],password=hashed_password,birthday=postData['birthday'])
				print new_user
				result['status'] = True
				result['user_id'] = new_user.id
				
			else:	
				print "You are already a user, please log in"
				errors['not_new'] = "You are already a user, please log in"
		result['errors'] = errors			
		return result

	def login_validation(self,postData):
		errors = {}
		result = {
			'status':True
		}
		email_database = User.objects.filter(email=postData['email'])
		print email_database
		
		if(len(email_database) == 1):
			result['user_id'] = email_database[0].id
			print "Email found in database"
			print email_database[0]
			hash_database = email_database[0].password
			if(bcrypt.checkpw(postData['password'].encode(), hash_database.encode())):
				print "Passwords match!"
			else:
				result['status'] = False
				errors['login']	= "Wrong Password!"
		else:
			result['status'] = False
			errors['login'] = "Email not found. Try Registering?"		
		result['errors'] = errors	
		return result		
	
# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	birthday = models.DateTimeField()
	password = models.CharField(max_length=300)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	def __repr__(self):
		return "<Rest_User object: {} {}>".format(self.name,self.alias,self.email)
	
	objects = Rest_UserManager()