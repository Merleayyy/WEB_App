# 学习笔记

这是一个名为“学习笔记”的web应用程序，让用户能够记录感兴趣的主题，并在学习每个主题的过程中添加日志条目。“学习笔记”的主页对这个网站进行描述，并邀请用户注册或者登陆。用户登陆后，就可创建新主题、添加新条目以及阅读既有的条目。

---

## 在Windows下创建一个虚拟环境

```python
python - m venv ll_env # 创建了一个名为ll_env的虚拟环境
ll_env\Scripts\activate # 进入这个虚拟环境
# 如果需要退出执行
deactivate
```

## 在Django中创建项目

```python
django-admin startproject learning_log .
# 这里创建了一个名为learning_log的项目
```

## 创建数据库

```python
python manage.py migrate
```

## 检测项目是否正常运行/启动项目

```python
python manage.py runserver # 每次进入网页都必须先启动
```

---

## 创建应用程序

```python
# 在虚拟环境的条件下,执行
python manage.py startapp learning_logs
# 这里创建了一个名为learning_logs的应用程序
```

### 创建模型/创建数据交互

1. 定义模型

   ```python
   models.py
   class Topic(models.Model):
       # 设置text的属性为文本属性，之后传入的数据为文本数据
   	text = models.TextField()
       # 加入一个时间戳，每次调用模型时记录一个时间戳
       date_added = models.DateTimeField(auto_now_add = True)
   	def __str__(self):
   		# 返回模型名字的字符串表示,也就代表着这个对象本身的值
           # 也就是调用对象时的值（主键）
   		return self.text
   ```

2. 激活模型

   ```python
   settings.py
   INSTALLED_APPS = [
   	--snip--
       # 我自己的应用程序,注意这里是声明应用程序文件
       'learning_logs',
   ]
   ```

   ```python
   # 执行
   python manage.py makemigrations learning_logs
   python manage.py migrate
   ```

3. 建立超级用户

   ```python
   python manage.py createsuperuser
   ```

4. 向管理网站**注册模型**

   ```python
   admin.py
   --snip--
   from learning_logs.models import Topic
   
   admin.site.register(Topic)
   ```

### 创建多个模型重复执行上述1,2,4步

---

## 管理**URL**

### 项目URL

```python
urls.py--learning_log
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
urlpatterns = [
    # 当网址为xxxx/admin时，链接到admin.site.urls这个网站中（自动生成）
    path('admin/', admin.site.urls),
    
    # 其他情况则由learning_logs中的urls决定
    url(r'', include(("learning_logs.urls", 'learning_logs'), namespace = 'learning_logs')),
]
```

### 应用程序URL

```python
urls.py--learning_logs

from django.contrib import admin
from django.conf.urls import include, url

from . import views
urlpatterns = [
	# 主页,也就是没有任何后缀时调用views.index
	url(r'^$', views.index, name = 'index'),
	# 网站后缀名为topics/调用views.topics
	url(r'^topics/$', views.topics, name = 'topics'),

	# 
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic')
]
```

```python
views.py
from django.shortcuts import render

from .models import Topic
# views是用于收集好网页所需要的数据，然后再将其传送给网页
def index(request):
	# 在匹配到网址后，调用这里的函数
    # 执行index.html
	return render(request, 'learning_logs/index.html')

def topics(request):
	topics = Topic.objects.order_by('date_added') # 取得Topic对象，并按照date_added进行排序
    
    # 为了能在html中使用python中的变量，定义变量topics为上面的topics
	context = {'topics': topics} 
    # 传入html文件中通过context
	return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
	# 显示单个主题及其所有的条目
	topic = Topic.objects.get(id = topic_id)
	entries = topic.entry_set.order_by('-date_added') # entry_set能返回一个topic关联对象的列表
	context = {'topic':topic, 'entries':entries}
	return render(request, 'learning_logs/topic.html', context)


```

```html
learning_logs\templates\learning_logs\base.html

<p>
	<!-- 匹配到learning_logs.urls中的各个网址 -->
	<a href="{% url 'learning_logs:index' %}">Learning Log</a>
	<a href="{% url 'learning_logs:topics' %}">Topics</a>
</p>

{% block content %}{% endblock content %}

index.html
<!-- 继承base.html -->
{% extends "learning_logs/base.html" %} 

{% block content %}
	<h1>Learning Log</h1>
	<p>Learning Log helps you keep track of your learning, for any topic you're learning about.</p>
{% endblock content %}

topic.html
{% extends "learning_logs/base.html" %}

{% block content %}
	<p>Topic: {{topic}}</p>

	<p>Entries:</p>
	
	<ul>
		{% for entry in entries %}
			<li>
				<p>{{ entry.date_added|date:'M d, Y H:i' }}</p>
				<p>{{ entry.text|linebreaks}}</p>
			</li>
				{% empty %}
			<li>
				No topics have been added yet.
			</li>

		{%endfor%}
	</ul>
{% endblock content %}


topics.html
{% extends "learning_logs/base.html" %}
{% block content %}
	<p>Topics</p>
	<ul>
		{% for topic in topics %}
			<li><a href="{% url 'learning_logs:topic' topic.id %}">{{ topic }} {{ name }}</a></li>
		{% empty %}
			<li>No topics have been added yet.</li>
		{%endfor%}
	</ul>
{% endblock content %}


```

