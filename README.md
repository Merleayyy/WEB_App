这是一个名为“学习笔记”的web应用程序，让用户能够记录感兴趣的主题，并在学习每个主题的过程中添加日志条目。“学习笔记”的主页对这个网站进行描述，并邀请用户注册或者登陆。用户登陆后，就可创建新主题、添加新条目以及阅读既有的条目。

---

### 在Windows下创建一个虚拟环境

```python
python - m venv ll_env # 创建了一个名为ll_env的虚拟环境
ll_env\Scripts\activate # 进入这个虚拟环境
# 如果需要退出执行
deactivate
```

### 在Django中创建项目

```python
django-admin startproject learning_log .
# 这里创建了一个名为learning_log的项目
```

### 创建数据库

```python
python manage.py migrate
```

### 检测项目是否正常运行

```python
python manage.py runserver
```

