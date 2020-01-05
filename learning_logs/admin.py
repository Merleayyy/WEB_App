from django.contrib import admin

from learning_logs.models import Topic, Entry, Pizza, Topping

from learning_logs.models import Entry

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Pizza)
admin.site.register(Topping)

# Register your models here.
