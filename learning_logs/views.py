from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(request):
	# 学习笔记的主页
	return render(request, 'learning_logs/index.html')

def topics(request):
	# 显示所有的主题
	topics = Topic.objects.order_by('date_added') # 取得Topic对象，并按照date_added进行排序
	my_name = "huzhiyong"
	print(topics)
	context = {'topics': topics, 'name':my_name}
	return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
	# 显示单个主题及其所有的条目
	topic = Topic.objects.get(id = topic_id)
	entries = topic.entry_set.order_by('-date_added') # entry_set能返回一个topic关联对象的列表
	context = {'topic':topic, 'entries':entries}
	return render(request, 'learning_logs/topic.html', context)