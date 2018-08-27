from django.shortcuts import render
from django.conf.urls import url,include
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser,FormParser
from .models import *
from .serializers import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from django.contrib.auth.decorators import login_required


#Login view without authentication
#@login_required(login_url="login/")
def home(request):
	return render(request, "home.html")

def exam_marks(request):
	# Exam Marks URL
	return render(request, "exam_marks.html")

def attendance(request):
	# Attendance URL
	return render(request, "attendance.html")


#DepartmentApi()
@csrf_exempt
@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))

def departmentApi(request):
	if request.method == 'GET':
		#Check is user is Staff or Superuser
		if not request.user.is_staff or not request.user.is_superuser:
			return JsonResponse({'error':'You are not authorized to do this operation.'},status=status.HTTP_401_UNAUTHORIZED)
		if 'name' in request.GET:
			department = Department.objects.filter(name=request.GET['name'])
		else:
			department = Department.objects.all()
		serializer = DepartmentSerializer(department, many=True)
		return JsonResponse(serializer.data,safe=False)
	elif request.method == 'POST':

		if not request.user.is_staff or not request.user.is_superuser:
			return JsonResponse({'error':'You are not authorized to do this operation.'},status=status.HTTP_401_UNAUTHORIZED)
		data=''
		if 'name' in request.POST:
			data = {'name':request.POST['name']}
		else:
			return JsonResponse({'error': 'Please provide department name'},
            status=status.HTTP_400_BAD_REQUEST)

		serializer = DepartmentSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)
#End departmentApi

#courseApi()
@csrf_exempt
@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))

def courseApi(request):
	print(request.user.is_staff)
	if request.method == 'GET':
		#Check is user is Staff or Superuser
		if not request.user.is_staff or not request.user.is_superuser:
			return JsonResponse({'error':'You are not authorized to do this operation.'},status=status.HTTP_401_UNAUTHORIZED)
		if 'name' in request.GET:
			# print(request.GET.get('name'))
			course = Course.objects.filter(name=request.GET['name'])
		elif 'duration' in request.GET:
			# print(request.GET.get('duration'))
			course = Course.objects.filter(duration__gte=request.GET['duration'])
		else:
			course = Course.objects.all()
		serializer = CourseSerializer(course, many=True)
		return JsonResponse(serializer.data,safe=False)
	elif request.method == 'POST':
		#CHecking if user is Staff or Super User

		print(request.POST['name'])

		if not request.user.is_staff or not request.user.is_superuser:
			return JsonResponse({'error':'You are not authorized to do this operation.'},status=status.HTTP_401_UNAUTHORIZED)

		#Declaring data which will be useful to store a dictionary
		data=''
		if ('name' in request.POST and 'duration' in request.POST and 'department_id' in request.POST) :
			data = {'name':request.POST['name'],
					'duration':request.POST['duration'],
					'department_id':request.POST['department_id']}
		else:
			return JsonResponse(
            {'error': 'Please pass name, duration, department_id'},
            status=status.HTTP_400_BAD_REQUEST)
		serializer = CourseSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)
#End courseApi


#Parent API only GET for now
# @csrf_exempt
# @login_required
# @api_view(['GET', 'POST'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))

# def parentApi(request):
# 	#Checking if data is coming from GET method
# 	if request.method == 'GET':

# 		if not request.user.is_staff or not request.user.is_superuser:
# 			return JsonResponse({'error':'You are not authorized to do this operation.'},status=status.HTTP_401_UNAUTHORIZED)

# 		if 'username' in request.GET:
# 			try: #to handle exception
# 				parents = Parent.objects.get(user = User.objects.get(username = request.GET['username']))
# 				serializer = ParentSerializer(parents)
# 				print(parents)
# 			except ObjectDoesNotExist:
# 				return JsonResponse(
#             {'error': 'No data found for user '+request.GET['username']},
#             status=status.HTTP_200_OK)
# 		else:
# 			parents = Parent.objects.all()
# 			serializer = ParentSerializer(parents, many=True)
# 		return JsonResponse(serializer.data,safe=False)
# 	elif request.method == 'POST': #Checking if Data is coming from POST
# 		if request.user.is_staff or not request.user.is_superuser:
# 			return JsonResponse({'error':'You are not authorized to do this operation.'},status=status.HTTP_401_UNAUTHORIZED)
# 			data=''
# 			if ('username' in request.POST and 'password' in request.POST and 'email' in request.POST and 'first_name' in request.POST and
# 				 'last_name' in request.POST and 'contact' in request.POST and 'address' in request.POST):
# 				user = User.objects.create_user(username = request.POST['username'],
# 					password = request.POST['password'],email = request.POST['email'],first_name = request.POST['first_name'],
# 					last_name = request.POST['last_name'])
# 				data = {'user':user.id,'contact':request.POST['contact'],'address':request.POST['address']}
# 			else:
# 				return JsonResponse(
# 	            {'error': 'Please pass Required fields'},
# 	            status=status.HTTP_400_BAD_REQUEST)
# 			serializer = ParentSerializer(data=data)
# 			if serializer.is_valid():
# 				serializer.save()
# 				return JsonResponse(serializer.data, status=201)
# 			return JsonResponse(serializer.errors, status=400)
# 		else:
# 			return JsonResponse(
# 	            {'error': 'You are not authorized to do this Operation'},
# 	            status=status.HTTP_401_UNAUTHORIZED)
# #End Parent API



#Parent API only GET for now
@csrf_exempt
# @login_required
@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def parentApi(request):
	#Checking if data is coming from GET method
	if request.method == 'GET':

		# if not request.user.is_staff or not request.user.is_superuser:
		# 	return JsonResponse({'error':'You are not authorized to do this operation.'},status=status.HTTP_401_UNAUTHORIZED)

		if 'username' in request.GET:
			try: #to handle exception
				parents = Parent.objects.get(user = User.objects.get(username = request.GET['username']))
				serializer = ParentSerializer(parents)
				# student = Student.objects.filter(parent=)
				id = serializer.data['id']
				studentsData = Student.objects.filter(parent = id)
				studentSerializer = StudentSerializer(studentsData,many=True)

				data = {'parent':serializer.data,'children':studentSerializer.data}
				return JsonResponse(data)
			except ObjectDoesNotExist:
				return JsonResponse(
            {'error': 'No data found for user '+request.GET['username']},
            status=status.HTTP_200_OK)
		else:
			parents = Parent.objects.all()
			serializer = ParentSerializer(parents, many=True)
			return JsonResponse(serializer.data,safe=False)
	elif request.method == 'POST': #Checking if Data is coming from POST
		if request.user.is_staff or not request.user.is_superuser:
			return JsonResponse({'error':'You are not authorized to do this operation.'},status=status.HTTP_401_UNAUTHORIZED)
			data=''
			if ('username' in request.POST and 'password' in request.POST and 'email' in request.POST and 'first_name' in request.POST and
				 'last_name' in request.POST and 'contact' in request.POST and 'address' in request.POST):
				user = User.objects.create_user(username = request.POST['username'],
					password = request.POST['password'],email = request.POST['email'],first_name = request.POST['first_name'],
					last_name = request.POST['last_name'])
				data = {'user':user.id,'contact':request.POST['contact'],'address':request.POST['address']}
			else:
				return JsonResponse(
	            {'error': 'Please pass name, duration, department_id'},
	            status=status.HTTP_400_BAD_REQUEST)
			serializer = ParentSerializer(data=data)
			if serializer.is_valid():
				serializer.save()
				return JsonResponse(serializer.data, status=201)
			return JsonResponse(serializer.errors, status=400)
		else:
			return JsonResponse(
	            {'error': 'You are not authorized to do this Operation'},
	            status=status.HTTP_401_UNAUTHORIZED)
#End Parent API




#Student Api
@csrf_exempt
@login_required
@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def studentApi(request):
	#Checking if data is coming from GET method
	if request.method == 'GET':

		if not request.user.is_staff or not request.user.is_superuser:
			return JsonResponse({'error':'You are not authorized to do this operation.'},status=status.HTTP_401_UNAUTHORIZED)

		if 'username' in request.GET:
			try: #to handle exception
				student = Student.objects.get(user = User.objects.get(username = request.GET['username']))
				serializer = StudentSerializer(student)
				print(student)
			except ObjectDoesNotExist:
				return JsonResponse(
            {'error': 'No data found for user '+request.GET['username']},
            status=status.HTTP_200_OK)
		else:
			student = Student.objects.all()
			serializer = StudentSerializer(student, many=True)
		return JsonResponse(serializer.data,safe=False)
	elif request.method == 'POST': #Checking if Data is coming from POST
		if request.user.is_staff or not request.user.is_superuser:
			return JsonResponse({'error':'You are not authorized to do this operation.'},status=status.HTTP_401_UNAUTHORIZED)
			data=''
			if ('username' in request.POST and 'password' in request.POST and 'email' in request.POST and 'first_name' in request.POST and
				 'last_name' in request.POST and 'contact' in request.POST and 'address' in request.POST and 'parent_id' in request.POST and 'course_id' in request.POST):
				user = User.objects.create_user(username = request.POST['username'],
					password = request.POST['password'],email = request.POST['email'],first_name = request.POST['first_name'],
					last_name = request.POST['last_name'])
				data = {'user':user.id,'contact':request.POST['contact'],'address':request.POST['address'],'parent_id':parent_id,'course_id':course_id}
			else:
				return JsonResponse(
	            {'error': 'Please pass required fields'},
	            status=status.HTTP_400_BAD_REQUEST)
			serializer = StudentSerializer(data=data)
			if serializer.is_valid():
				serializer.save()
				return JsonResponse(serializer.data, status=201)
			return JsonResponse(serializer.errors, status=400)
		else:
			return JsonResponse(
	            {'error': 'You are not authorized to do this Operation'},
	            status=status.HTTP_401_UNAUTHORIZED)



#SubjectApi
@csrf_exempt
# @login_required
@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def subjectApi(request):
	print(request.user.is_staff)
	if request.method == 'GET':
		#Check is user is Staff or Superuser
		if not request.user.is_staff or not request.user.is_superuser:
			return JsonResponse({'error':'You are not authorized to do this operation.'},status=status.HTTP_401_UNAUTHORIZED)
		if 'name' in request.GET:
			subject = Subject.objects.filter(name=request.GET['name'])
		else:
			subject = Subject.objects.all()
		serializer = SubjectSerializer(subject, many=True)
		return JsonResponse(serializer.data,safe=False)

	# elif request.method == 'POST':

	# 	if not request.user.is_superuser:
	# 		return JsonResponse({'error':'You are not authorized to do this operation.'},status=status.HTTP_401_UNAUTHORIZED)
	# 	data=''
	# 	if ('name' in request.POST and 'course_id' in request.POST and 'teacher_id' in request.POST) :
	# 		data = {'name':request.POST['name'],
	# 				'course_id':request.POST['course_id'],
	# 				'teacher_id':request.POST['teacher_id']
	# 				}
	# 	else:
	# 		return JsonResponse({'error': 'Please provide subject name'},
 #            status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'POST':

		if request.user.is_superuser:

			# data=''
			if ('name' in request.POST and 'course_id' in request.POST and 'teacher_id' in request.POST) :
				data = {'name':request.POST['name'],
						'course_id':request.POST['course_id'],
						'teacher_id':request.POST['teacher_id']
						}

			else:
				return JsonResponse({'error': 'Please provide subject name'},
            		status=status.HTTP_400_BAD_REQUEST)


		else:
			return JsonResponse({'error':'You are not authorized to do this operation.'},status=status.HTTP_401_UNAUTHORIZED)


		serializer = SubjectSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)
#End SubjectApi



#Exam Api
@csrf_exempt
@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def examApi(request):
	# print(request.user.is_staff)
	if request.method == 'GET':
		#Check is user is Staff or Superuser
		if not request.user.is_staff or not request.user.is_superuser:
			return JsonResponse({'error':'You are not authorized to do this operation.'},status=status.HTTP_401_UNAUTHORIZED)
		if 'title' in request.GET:
			exam = Exam.objects.filter(title=request.GET['title'])
		elif 'batch' in request.GET:
			exam = Exam.objects.filter(batch=request.GET['batch'])
		elif 'id' in request.GET:
			try: #to handle exception
				exam = Exam.objects.filter(course = request.GET['id'])
				# exam = Exam.objects.filter(batch=request.GET['batch'])
				#serializer = ExamSerializer(exams)
				#print(parents)
			except ObjectDoesNotExist:
				return JsonResponse(
            {'error': 'No data found for exam '+request.GET['name']},
            status=status.HTTP_200_OK)
		else:
			exam = Exam.objects.all()
		serializer = ExamSerializer(exam, many=True)
		return JsonResponse(serializer.data,safe=False)

	elif request.method == 'POST':

		if not request.user.is_superuser:
			return JsonResponse({'error':'You are not authorized to do this operation.'},status=status.HTTP_401_UNAUTHORIZED)
		data=''
		if ('title' in request.POST and 'batch' in request.POST and 'course_id' in request.POST and 'teacher_id' in request.POST) :
			data = {'title':request.POST['title'],
					'batch':request.POST['batch'],
					'course_id':request.POST['course_id'],
					'teacher_id':request.POST['teacher_id']
					}
		else:
			return JsonResponse({'error': 'Please provide exam name'},
            status=status.HTTP_400_BAD_REQUEST)

		serializer = ExamSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)


#EndExam Api



# #Exam_Subject Api
# @csrf_exempt
# @api_view(['GET', 'POST'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))

# def examSubjectApi(request):
# 	print(request.user.is_staff)
# 	if request.method == 'GET':
# 		#Check is user is Staff or Superuser
# 		if 'marks' in request.GET:
# 			marks = ExamSubject.objects.filter(marks=request.GET['marks'])
# 		else:
# 			marks = ExamSubject.objects.all()
# 		serializer = ExamSubjectSerializer(marks, many=True)
# 		return JsonResponse(serializer.data,safe=False)
# 	elif request.method == 'POST':
# 		# We got POST request Now Insert Data into DB
# 		if not request.user.is_staff or not request.user.is_superuser:
# 			return JsonResponse({'error':'You are not authorized to do this operation.'},status=status.HTTP_401_UNAUTHORIZED)
# 		data = ''
# 		if 'marks' in request.POST and 'subject_id' in request.POST and 'exam_id' in request.POST and 'student_id' in request.POST and 'exam_date' in request.POST:
# 			data = {'marks':request.POST['marks'],
# 			'subject':request.POST['subject_id'],
# 			'exam':request.POST['exam_id'],
# 			'student':request.POST['student_id'],
# 			'exam_date':request.POST['exam_date']
# 			}
# 		else:
# 			return JsonResponse({'error': 'Please provide details'},status=status.HTTP_400_BAD_REQUEST)

# 		serializer = ExamSubjectSerializer(data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JsonResponse(serializer.data, status=201)
# 		return JsonResponse(serializer.errors, status=400)
# #End ExamSubject API

#Attendance API
@csrf_exempt
@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def attendanceApi(request):
    if request.method == 'GET':

        if 'student_name' in request.GET and 'start_date' in request.GET and 'end_date' in request.GET:
            userData = User.objects.get(username = request.GET['student_name'])
            # print(studentData.id)
            attendance = Attendance.objects.filter(student=Student.objects.get(user=userData),date__gte=request.GET['start_date'],date__lte=request.GET['end_date'])
            serializer = AttendanceSerializer(attendance,many=True)
            return JsonResponse(serializer.data,safe=False)
        else:
            attendance = Attendance.objects.all()
            serializer = AttendanceSerializer(attendance,many=True)
            return JsonResponse(serializer.data,safe=False)
        return JsonResponse({'error':'Please Provide Valid Data'}, status=status.HTTP_400_BAD_REQUEST)
#End Attendance API

#subjectMarksApi
@csrf_exempt
@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def subjectMarksApi(request):
    if request.method == 'GET':
        if 'student_name' in request.GET and 'title' in request.GET and 'year' in request.GET:
            userData = User.objects.get(username = request.GET['student_name'])
            student = Student.objects.get(user = userData)
            # course = Course.objects.get(name = student.course.name)
            exam = Exam.objects.filter(title = request.GET['title'],course = student.course)
            subjects = Subject.objects.filter(year = request.GET['year'])
            # print(course)


            examSubject = ExamSubject.objects.filter(student = student,subject__in = [s.id for s in subjects], exam__in = [e.id for e in exam])
            # examTitleSubject = examSubject.objects.filter(exam = 1)


            serializer = ExamSubjectSerializer(examSubject,many=True)
            return JsonResponse(serializer.data,safe=False)
        else:
            return JsonResponse({'error':'Please provide valid Data'},status=status.HTTP_400_BAD_REQUEST)

#End subjectMarksApi
