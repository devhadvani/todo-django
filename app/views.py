from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm

# Create your views here.
def home(request):
    fm = TodoForm()
    data = Todo.objects.all()
    if request.method == "POST":
        fm = TodoForm(request.POST)
        if fm.is_valid():
            fm.save()
            print("yes")
            messages.success(request,"insterted successfuly")
            fm = TodoForm()

        # name = request.GET['name']
        # user = Todo(name=name)
        # user.save()
    return render(request,"home.html",{"data":data,"form":fm})

def update(request,id):
    todo = Todo.objects.get(id=id)
    if request.method == "POST":
        fm = TodoForm(request.POST,instance=todo)
        if fm.is_valid():
            fm.save()
            return redirect('home')
    else:
        form =  TodoForm(instance=todo)
    return render(request,'update.html',{"form":form})

def delete(request,id):
    # if request.method =="GET":
    record = Todo.objects.get(id=id)
    record.delete()
    messages.success(request,"deleted successfuly")

    return redirect('home')

def done(request,id):
    record = Todo.objects.get(id=id)
    record.complete = True
    record.save()
    return redirect('home')
    # return reb