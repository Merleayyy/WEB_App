# Generated by Django 3.0 on 2020-01-05 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_pizza_topping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topping',
            name='pizza',
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
        migrations.DeleteModel(
            name='Topping',
        ),
    ]
