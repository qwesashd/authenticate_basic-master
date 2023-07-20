from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect
from .models import Task, Support
from users.forms import UserCreationForm, MyForm, SupportForm
from users import forms



def support(request):
    user = request.user
    if request.method == 'POST':
        form = SupportForm(request.POST)
        support = Support()
        if form.is_valid():
            text = form.cleaned_data['text']
            support.nickname = user.username
            support.email = user.email
            support.text = text
            support.save()
            return redirect('send')
    else:
        form = SupportForm()
    return render(request, 'support.html', {'form': form, 'nickname': user.username, 'email': user.email})


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

def children(request):
    user = request.user
    if request.method == 'POST':
        form = MyForm(request.POST)
        task = Task()
        if form.is_valid():
            name = form.cleaned_data['id_task']
            task.nickname = user.username
            task.task_complited = name
            task.save()
            return redirect('children')
    else:
        form = MyForm()
    return render(request, 'registration/children.html', {'form': form})

def teen(request):
    user = request.user
    if request.method == 'POST':
        form = MyForm(request.POST)
        task = Task()
        if form.is_valid():
            name = form.cleaned_data['id_task']
            task.nickname = user.username
            task.task_complited = name
            task.save()
            return redirect('teen')
    else:
        form = MyForm()
    return render(request, 'registration/teen.html', {'form': form})

def Profile(request):
    user = request.user
    nickname = user.username
    task=Task.objects.filter(nickname=nickname)
    list_task_child=[]
    list_task_teenage = []
    for task_id in range(len(task)):
        if task[task_id].task_complited >= 1 and task[task_id].task_complited <= 15 and task[task_id].task_complited not in list_task_child:
            list_task_child.append(task[task_id].task_complited)
        if task[task_id].task_complited >= 16 and task[task_id].task_complited <= 30and task[task_id].task_complited not in list_task_teenage:
            list_task_teenage.append(task[task_id].task_complited)
    com_child = len(list_task_child)
    com_teenage = len(list_task_teenage)
    percent_child = int((com_child / 15) * 100)
    percent_teenage = int((com_teenage/15)*100)
    return render(request,'registration/profile.html', {'nickname': nickname, 'percent_child': percent_child, 'percent_teenage':percent_teenage, 'list_task_teenage':list_task_teenage,'list_task_child':list_task_child})




def send(request):
    return render(request, 'send.html')

def choose(request):
    return render(request, 'choose.html')

def disk(request):
    return render(request, 'disk.html')

