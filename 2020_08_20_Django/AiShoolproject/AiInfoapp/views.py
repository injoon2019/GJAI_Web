from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import AiClass, AiStudent
# Create your views here.

def home(request):

    classes = AiClass.objects.all()
    context = {
        'classes':classes
    }
    return render(request, 'home.html', context)

def detail(request, class_pk):
    print(class_pk)

    class_obj = AiClass.objects.get(pk=class_pk)
    student_obj = AiStudent.objects.filter(class_num = class_pk)

    context= {
        'class_pk': class_pk,
        'class_obj': class_obj,
        'student_obj': student_obj
    }
    return render(request, 'detail.html', context)

def add(request, class_pk):
    
    class_obj = AiClass.objects.get(pk=class_pk)

    if request.method=="POST":

        AiStudent.objects.create(
            class_num= class_pk,
            name=request.POST['name'],
            phone_num = request.POST['phone_num'],
            intro_text = request.POST['intro_text']
        )

        return redirect('detail', class_pk)
    
    context={
        'class_obj': class_obj
    }

    return render(request, 'add.html', context)

def edit(request, student_pk):

    if request.method=="POST":

        AiStudent.objects.filter(pk=student_pk).update(
            name=request.POST['name'],
            phone_num = request.POST['phone_num'],
            intro = request.POST['intro']
        )
        return redirect('student', student_pk)
    
    student = AiStudent.objects.get(pk=student_pk)

    context = {
        'student': student
    }

    return render(request, 'edit.html', context)


def delete(request, class_num, student_pk):
    #삭제하기
    target_student = AiStudent.objects.get(pk=student_pk)
    target_student.delete()

    class_pk = class_num

    return redirect('detail', class_pk)