from __future__ import unicode_literals
from django.db import models


# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # agregue claves y valores al diccionario de errores para cada campo no válido
        if len(postData["name"]) < 5:
            errors["name"] = "El titulo debe tener al menos 5 caracteres"
        if len(postData['desc']) < 15:
            errors["desc"] = "La descripcion debe tener al menos 15 caracteres"
        return errors



class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()


class Desc(models.Model):
    desc = models.CharField(max_length=255)
    course = models.OneToOneField(Course, related_name="desc", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
