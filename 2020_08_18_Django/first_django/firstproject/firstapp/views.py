from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
students = ['최주원', '홍길동', '세종대왕']

def home(request):
    chat = 'Hello'
    name= "Injun"
    return render(request, 'home.html', {'user_chat':chat, 'user_name':name})

def login(request):
    return HttpResponse('Login!')

def signout(request):
    return HttpResponse('signout')

def result(request):
    name = request.POST['username']

    if name in students:
        is_exist = True
    else:
        is_exist = False
    return render(request, 'result.html', {'user_name': name, 'is_exist': is_exist})

def count(request):
    return render(request, 'count.html')

def count_result(request):
    line = request.POST['sentence']
    cha_num = len(line)
    return render(request, 'count_result.html', {'count':cha_num})