# 定义learning_logs的URL模式

from django.contrib import admin
from django.conf.urls import include, url

from . import views
urlpatterns = [
	# 主页
	url(r'^$', views.index, name = 'index'),
	
	url(r'^topics/$', views.topics, name = 'topics'),

	# 特定的主题界面
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic')
    # path('', views.index, name = 'index'),
    # path('topic/', views.topics, name = 'topics')
]