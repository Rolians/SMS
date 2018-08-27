from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

#Department Model
class Department(models.Model):
	name = models.CharField(max_length=80, unique=True)

	def __str__(self):
		return self.name;

#Course Model
class Course(models.Model):
    name = models.CharField(max_length=50)
    duration = models.IntegerField()
    department = models.ForeignKey(Department ,on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + self.department.name

#Parent Model
class Parent(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	contact = models.BigIntegerField()
	address = models.CharField(max_length=500)

	def __str__(self):
		return self.user.first_name+' '+self.user.last_name

#Student Model
class Student(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	address = models.CharField(max_length=500)
	contact = models.BigIntegerField()
	parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
	course = models.ForeignKey(Course , on_delete=models.CASCADE)

	def __str__(self):
		return self.user.first_name+' '+self.user.last_name +' Son of '+self.parent.user.first_name+' '+self.parent.user.last_name

#Teacher Model
class Teacher(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	department = models.ForeignKey(Department,on_delete = models.CASCADE)

	def __str__(self):
		return self.user.first_name+' '+self.user.last_name

YEAR_CHOICES = [('FY', 'FY'), ('SY', 'SY'), ('TY', 'TY')]

#Subject Model
class Subject(models.Model):
	name = models.CharField(max_length=50)
	course = models.ForeignKey(Course , on_delete=models.CASCADE)
	teacher = models.ForeignKey(Teacher , on_delete=models.CASCADE)
	year = models.CharField(max_length = 2,choices = YEAR_CHOICES)


	def __str__(self):
		return self.name+' Added By '+self.teacher.user.first_name+''+self.teacher.user.last_name


#Exam Model
class Exam(models.Model):
	title = models.CharField(max_length=80)
	batch = models.CharField(max_length=80)
	course = models.ForeignKey(Course , on_delete=models.CASCADE)
	teacher = models.ForeignKey(Teacher , on_delete=models.CASCADE)

	def __str__(self):
		return self.title+' Added By '+self.teacher.user.first_name+''+self.teacher.user.last_name

#ExamSubject Model
class ExamSubject(models.Model):
	marks = models.FloatField()
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
	exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	exam_date = models.DateTimeField()

	def __str__(self):
		return self.subject.name + " " + self.exam.title+' For student '+self.student.user.first_name+' Marks '+str(self.marks)

ATTENDANCE_STATUS = [('P','P'),('A','A')]

# class Attendance(models.Model):
class Attendance(models.Model):
	date = models.DateTimeField()
	student = models.ForeignKey(Student , on_delete=models.CASCADE)
	status = models.CharField(max_length=1, choices = ATTENDANCE_STATUS)
	remark = models.CharField(max_length=20)
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	subject = models.ForeignKey(Subject , on_delete=models.CASCADE)

	def __str__(self):
		return self.status
