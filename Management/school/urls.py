from django.conf.urls import url,include
from school.views import *

urlpatterns = [
    url(r'^department/$', departmentApi),
    url(r'^course/$', courseApi),
    url(r'^parent/$', parentApi),
    url(r'^parent/$', studentApi),
    url(r'^subject/$',subjectApi),
    url(r'^exam/$',examApi),
    url(r'^marks/$',subjectMarksApi),
    url(r'^attendanceapi/$',attendanceApi),
    url(r'^$', home , name = 'home'),
    url(r'^exam_marks/$', exam_marks , name = 'exam_marks'),
    url(r'^attendance/$', attendance , name = 'attendance')


]
