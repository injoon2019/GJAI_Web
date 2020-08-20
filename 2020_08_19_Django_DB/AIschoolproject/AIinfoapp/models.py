from django.db import models

# Create your models here.

class AiClass(models.Model):
    class_num = models.IntegerField()
    lecturer = models.CharField(max_length=30)
    class_room = models.CharField(max_length=30)
    students_num = models.IntegerField()

class AiStudents(models.Model):
    name =  models.CharField(max_length=30)
    phone_num = models.CharField(max_length=30)
    intro_text = models.TextField()
