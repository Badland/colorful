from django.db import models
from datetime import date

# Create your models here.

class User (models.Model) :
	MALE="M"
	FEMALE="F"
	NO_ANSWER="N"
	GENDER = [
		(MALE, "Male"),
		(FEMALE, "Female"),
		(NO_ANSWER,"No answer")
	]

	pseudo=models.CharField(max_length=30)
	gender=models.CharField(
		max_length=1,
		choices= GENDER,
		default=NO_ANSWER)

	mail_adress = models.CharField(max_length=320)
	date_joined=models.DateTimeField(default=date.today)


class Color (models.Model):
	r=models.PositiveIntegerField()
	g=models.PositiveIntegerField()
	b=models.PositiveIntegerField()	
	hex=models.CharField(max_length=7)
	name=models.CharField(max_length=30)

class Round (models.Model):
	date=models.DateTimeField()
	user_id=models.PositiveIntegerField()
	choice1=models.PositiveIntegerField()
	choice2=models.PositiveIntegerField()
	choice3=models.PositiveIntegerField()
	ans1=models.PositiveIntegerField()
	ans2=models.PositiveIntegerField()
	ans3=models.PositiveIntegerField()
	score=models.IntegerField()

