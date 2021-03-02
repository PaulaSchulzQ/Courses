from django.shortcuts import render, HttpResponse, redirect
from .models import Course, Desc
from django.contrib import messages
from time import gmtime, strftime

# Create your views here.
def index(request):
    context = {
        "courses": Course.objects.all(),
        "desc": Desc.objects.all(),

    }
    return render(request, "index.html", context)

def addcoursetitle(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        # si el diccionario de errores contiene algo, recorra cada par clave-valor y cree un mensaje flash
        for key, value in errors.items():
            messages.error(request, value)
        # redirigir al usuario al formulario para corregir los errores
        return redirect("/")
    else:
        if request.method == "POST":
            new_course = Course.objects.create(name=request.POST["name"])
            Desc.objects.create(desc=request.POST['desc'], course=new_course)

            return redirect("/")


def linkdest(request, c_id):
    context = {
        "courses_id": Course.objects.filter(id=c_id)
    }
    return render(request, "confirmdelete.html", context)


def remove(request, c_id):
    coursedelete = Course.objects.get(id=c_id)
    coursedelete.delete()
    return redirect('/')
