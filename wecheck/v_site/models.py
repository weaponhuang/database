from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Academys(models.Model):
	a_id = models.CharField(max_length=30,primary_key=True)
	a_name = models.CharField(max_length=50)
	def __str__(self):
		return self.a_name

class Subjects(models.Model):
	sub_id = models.CharField(max_length=30, primary_key=True)
	sub_name = models.CharField(max_length=50)
	sub_academy = models.ForeignKey(Academys)
	def __str__(self):
		return self.sub_name

class Homework(models.Model):
	Homework_id = models.IntegerField(null=True)
	hom_text = models.TextField()
	hom_date = models.DateField()

class Teachers(models.Model):
	tea_id = models.CharField(max_length=30, primary_key=True)
	tea_name = models.CharField(max_length=50)
	tea_email = models.CharField(max_length=50)
	tea_homework = models.ForeignKey(Homework,blank=True,null=True)
	def __str__(self):
		return self.tea_name

class Comment(models.Model):
	Comment_id = models.IntegerField(null=True)
	com_text = models.TextField()
	com_date = models.DateField()

class Courses(models.Model):
	cou_id = models.CharField(max_length=30, primary_key=True)
	cou_name = models.CharField(max_length=50)
	cou_time = models.CharField(max_length=50)
	cou_place = models.CharField(max_length=50)
	cou_property = models.CharField(max_length=50)
	cou_like = models.IntegerField(blank=True)
	cou_bad = models.IntegerField(blank=True)
	cou_subject = models.ForeignKey(Subjects)
	cou_teacher = models.ForeignKey(Teachers)
	cou_comment = models.ForeignKey(Comment,blank=True,null=True)
	cou_homework = models.ForeignKey(Homework,blank=True,null=True)
	def __str__(self):
		return self.cou_name

class Students(models.Model):
	stu_id = models.CharField(max_length=30, primary_key=True)
	stu_name = models.CharField(max_length=50)
	stu_email = models.CharField(max_length=50)
	stu_grade = models.CharField(max_length=50)
	stu_academy = models.ForeignKey(Academys)
	stu_course = models.ManyToManyField(Courses,blank=True)
	stu_comment = models.ForeignKey(Comment,blank=True, null=True)
	def __str__(self):
		return self.stu_name