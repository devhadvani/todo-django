from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm
# Create your views here.
def home(request):
    fm = TodoForm()
    data = Todo.objects.all()
    if request.method == "GET":
        fm = TodoForm(request.GET)
        name = request.GET["name"]
        user = Todo(name=name)
        user.save()
    return render(request,"home.html",{"data":data,"form":fm})