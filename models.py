from django.db import models

# Create your models here.
class order(models.Model):
	item=models.CharField(max_length=12)
	price=models.CharField(max_length=150)
	qn=models.IntegerField(default=10)


	class Student(model.Model):
		uname = models.CharField(max_length=20)
		fname = models.CharField(max_length=30)
		lname = models.CharField(max_length=30)
		mobile = models.CharField(max_length=10)
		email = models.EmailField()
