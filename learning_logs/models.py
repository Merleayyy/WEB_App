from django.db import models

# Create your models here.
class Topic(models.Model):
	# 用户学习的主题
	text = models.CharField(max_length = 200) # 设置text属性，CharField（length = x）由文本或者是字符组成的数据
	date_added = models.DateTimeField(auto_now_add = True)# 设置date_added属性，自动将时间设置为当前的时间

	def __str__(self):
		# 返回模型名字的字符串表示
		return self.text

class Entry(models.Model):
	# 学到的有关某个具体主题的具体知识
	topic = models.ForeignKey(Topic, on_delete = models.CASCADE)# 将Topic设置为外键
	text = models.TextField() # 设置text属性为不限制长度的文本
	date_added = models.DateTimeField(auto_now_add = True) # 加入一个时间戳，每次调用模型时记录一个时间戳

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		# 返回模型的字符串表示
		if len(self.text) > 50:
			return self.text[:50] + "..."
		else:
			return self.text

class Pizza(models.Model):
	name = models.CharField(max_length = 50)
	date_added = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		# 返回模型名字的字符串表示
		return self.name

class Topping(models.Model):
	pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
	name = models.CharField(max_length = 50)
	date_added = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		print(type(self.pizza))
		# 返回模型名字的字符串表示
		return self.name + '-Pizza:' + self.pizza.name

		