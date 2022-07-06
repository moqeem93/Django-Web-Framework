from django.shortcuts import render
from .forms import StudentForm
from .models import Students
from django.http import HttpResponseRedirect
# Create your views here.

def index(r):
    data = Students.objects.all()
    return render(r,'index.html',{'data':data})
def create(r):
    form = StudentForm()
    if r.method =='POST':
        form = StudentForm(r.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
    return render(r,'create.html',{'form':form})




