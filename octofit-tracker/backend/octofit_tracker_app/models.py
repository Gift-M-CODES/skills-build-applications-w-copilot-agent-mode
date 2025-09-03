from djongo import models

class User(models.Model):
	_id = models.ObjectIdField()
	email = models.EmailField(unique=True)
	name = models.CharField(max_length=100)
	password = models.CharField(max_length=128)
	# Add other fields as needed
	class Meta:
		app_label = 'octofit_tracker_app'

class Team(models.Model):
	_id = models.ObjectIdField()
	name = models.CharField(max_length=100)
	members = models.JSONField(default=list)
	# Add other fields as needed
	class Meta:
		app_label = 'octofit_tracker_app'

class Activity(models.Model):
	_id = models.ObjectIdField()
	user = models.CharField(max_length=100)
	activity_type = models.CharField(max_length=100)
	duration = models.IntegerField()
	timestamp = models.DateTimeField()
	# Add other fields as needed
	class Meta:
		app_label = 'octofit_tracker_app'

class Leaderboard(models.Model):
	_id = models.ObjectIdField()
	team = models.CharField(max_length=100)
	score = models.IntegerField()
	# Add other fields as needed
	class Meta:
		app_label = 'octofit_tracker_app'

class Workout(models.Model):
	_id = models.ObjectIdField()
	name = models.CharField(max_length=100)
	description = models.TextField()
	# Add other fields as needed
	class Meta:
		app_label = 'octofit_tracker_app'
from django.db import models

# Create your models here.
