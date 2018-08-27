from django.contrib import admin
from .models import *
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


admin.site.site_header = 'School Management'


class StudentAdmin(admin.ModelAdmin):
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'user':

			# if not request.user.is_superuser:

			# kwargs["queryset"] = Parent.objects.filter()

			kwargs["queryset"] = User.objects.filter(is_staff=False)

		return super(StudentAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
	list_display = ('id', 'user','contact','parent', 'address','course')
	list_filter = ('id','course','parent','user')


    
class TeacherAdmin(admin.ModelAdmin):
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		"""Limit choices for 'picture' field to only your pictures."""
		if db_field.name == 'user':
			# if not request.user.is_superuser:
			kwargs["queryset"] = User.objects.filter(is_staff=True)
		return super(TeacherAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

	list_display = ('id', 'user', 'department')
	list_filter = ('id','department')

class SubjectAdmin(admin.ModelAdmin):
	list_display = ('id','name','course','teacher','year')
	list_filter = ('name','course','teacher','year')

class CourseAdmin(admin.ModelAdmin):
	list_display = ('id','name','department','duration')
	list_filter = ('name','department','duration')

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ('id','name')
	list_filter = ('id','name')

class ParentAdmin(admin.ModelAdmin):
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'user':
			# if not request.user.is_superuser:
			kwargs["queryset"] = User.objects.filter(is_staff=False)
		return super(ParentAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
		
	list_display = ('id','user','contact','address')
	list_filter = ('id','user','contact')

class ExamAdmin(admin.ModelAdmin):
	list_display = ('id','title','batch','course','teacher')
	list_filter = ('id','title','batch','course','teacher')


class ExamSubjectAdmin(admin.ModelAdmin):
	list_display = ('id','marks','subject','exam','exam_date')
	list_filter = ('id','marks','subject','exam','exam_date')

class AttendanceAdmin(admin.ModelAdmin):
	list_display = ('id' , 'date' ,'student' , 'subject', 'status' , 'remark' , 'teacher')
	list_filter = ('id' , 'date' ,'student' , 'subject', 'status' )
# class SubjectCreationForm(forms.ModelForm):

admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Attendance , AttendanceAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Parent,ParentAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Exam,ExamAdmin)
admin.site.register(ExamSubject)
# admin.site.register(Attendance)
# Register your models here.
