from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('v_site.views',
	url(r'^$', 'home_handler', {'template_name':'home.html'}),
	url(r'^personal', 'personal_handler', {'template_name':'personal.html'}),
	url(r'^about', 'about_handler', {'template_name':'about.html'}),

	url(r'^login', 'request_login_handler', {'template_name':'login.html'}),
	url(r'^logout', 'request_logout_handler', {'template_name':'home.html'}),

	url(r'^check_course', 'check_course_handler', {'template_name':'check_course.html'}),

	url(r'^teacher$', 'teacher_handler', {'template_name':'teacher_home.html'}),
	url(r'^teacherper', 'teacherpersonal_handler', {'template_name':'teacher_personal.html'}),
	url(r'^homeworkre', 'homeworkre_handler', {'template_name':'homework_releasing.html'}),
	url(r'^teacherco', 'teacherco_handler', {'template_name':'teacher_check_course.html'}),
	)