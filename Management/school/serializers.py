from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

#Department Serializer
class DepartmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Department
		fields = '__all__'

#Course Serializer
class CourseSerializer(serializers.ModelSerializer):

	department = DepartmentSerializer(read_only=True)
	department_id = serializers.IntegerField(write_only=True)

	class Meta:
		many=True #find out what is many true??
		model = Course
		fields = ('id','name','duration','department','department_id')
		# depth = 1
	# department_name = DepartmentSerializer()

#Parent Srializer
class ParentSerializer(serializers.ModelSerializer):
	username = serializers.CharField(source='user.username',read_only=True)
	email = serializers.CharField(source='user.email',read_only=True)
	password = serializers.CharField(source='user.password',read_only=True)
	first_name = serializers.CharField(source='user.first_name',read_only=True)
	last_name = serializers.CharField(source='user.last_name',read_only=True)

	class Meta:
		many = True
		model = Parent
		fields = '__all__'

#Student Serializer
class StudentSerializer(serializers.ModelSerializer):
	username = serializers.CharField(source='user.username', read_only=True)
	email = serializers.CharField(source='user.username' , read_only=True)
	password = serializers.CharField(source='user.password' , read_only=True)
	first_name = serializers.CharField(source='user.first_name' , read_only=True)
	last_name = serializers.CharField(source='user.last_name' , read_only=True)

	class Meta:
		many = True
		model = Student
		fields = '__all__'

#Subject Serializer
class SubjectSerializer(serializers.ModelSerializer):

	course_id = serializers.IntegerField(write_only=True)
	teacher_id = serializers.IntegerField(write_only=True)

	class Meta:
		many = True
		model = Subject
		depth = 1
		fields = '__all__'


#Exam Serializer
class ExamSerializer(serializers.ModelSerializer):
	course_id = serializers.IntegerField(write_only=True)
	teacher_id = serializers.IntegerField(write_only=True)

	class Meta:
		many = True
		model = Exam
		depth = 1
		fields = '__all__'



#Exam_Subject Serializer
class ExamSubjectSerializer(serializers.ModelSerializer):

	student_first_name = serializers.CharField(source = 'student.user.first_name',read_only=True)
	student_last_name = serializers.CharField(source = 'student.user.last_name',read_only=True)
	student_main_id = serializers.CharField(source = 'student.user.id',read_only=True)
	student_username = serializers.CharField(source = 'student.user.username',read_only=True)

	teacher_first_name = serializers.CharField(source = 'exam.teacher.user.first_name',read_only=True)
	teacher_last_name = serializers.CharField(source = 'exam.teacher.user.last_name',read_only=True)
	teacher_main_id = serializers.CharField(source = 'exam.teacher.user.id',read_only=True)
	teacher_username = serializers.CharField(source = 'exam.teacher.user.username',read_only=True)


	exam_main_id = serializers.CharField(source = 'exam.id',read_only=True)
	exam_title = serializers.CharField(source = 'exam.title',read_only=True)
	exam_batch = serializers.CharField(source = 'exam.batch',read_only=True)
	exam_course = serializers.CharField(source = 'exam.course.name',read_only=True)
	exam_department = serializers.CharField(source = 'exam.course.department.name',read_only=True)

	subject_main_id = serializers.CharField(source = 'subject.id',read_only=True)
	subject_name = serializers.CharField(source = 'subject.name',read_only=True)



	# subject_id = serializers.IntegerField(write_only = True)
	# exam_id = serializers.IntegerField(write_only = True)
	# student_id = serializers.IntegerField(write_only = True)

	class Meta:
		 many = True
		 model = ExamSubject
		 fields = '__all__'
		 # fields = ('id','marks','subject_id','exam_id','student_id','student_main_id','student_username','student_first_name','student_last_name',
		 # 	'teacher_main_id','teacher_username','teacher_first_name','teacher_last_name',
		 # 	'exam_main_id','exam_title','exam_batch','exam_course','exam_department','subject_main_id','subject_name','exam_date')


#Attendance Serializer
class AttendanceSerializer(serializers.ModelSerializer):
	student_first_name = serializers.CharField(source = 'student.user.first_name',read_only=True)
	student_last_name = serializers.CharField(source = 'student.user.last_name',read_only=True)

	teacher_first_name = serializers.CharField(source = 'teacher.user.first_name',read_only=True)
	teacher_last_name = serializers.CharField(source = 'teacher.user.last_name',read_only=True)

	subject_name = serializers.CharField(source = 'subject.name',read_only=True)

	class Meta:
		many = True
		model = Attendance
		fields = '__all__'
