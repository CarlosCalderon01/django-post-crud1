# importar librerias
from django.shortcuts import render, redirect
# Importar Modelos
from .models import Task
# Create your views here.


def list_tasks(request):
    tasks = Task.objects.all()
    print(tasks)
    # envio la clase task como diccionario al html
    return render(request, 'list_tasks.html', {"tasks": tasks})


def create_task(request):
    # SIEMPRE ES MEJOR ENVIAR LOS DATOS A TRAVEZ DEL EMTODO POST Y NO POR URL
    task = Task(title=request.POST['title'],
                description=request.POST['description'])
    task.save()
    return redirect('/tasks/')


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks/')
