from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import StudentForm
from .models import Student
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
# Create your views here.
@login_required
def index_show(req):
    return render(req,'StudentRegistration/index.html')
def logout_show(req):
    return render(req,'StudentRegistation/logout.html')
def signup_show(req):
    form=forms.SignUpForm()
    if req.method=='POST':
        form=forms.SignUpForm(req.POST)
        user=form.save(commit=True)
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(req,'StudentRegistration/sign.html',{'form':form})
@login_required
def student_show(req):
    std_list=Student.objects.all()
    return render(req,'StudentRegistration/studentshow.html',{'std':std_list})
@login_required
def addstudent_show(req):
    form=StudentForm()
    if req.method=='POST':
        form=StudentForm(req.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/studentshow/')
    return render(req,'StudentRegistration/addstudent.html',{'form':form})

def delete(req,id):
    std=Student.objects.get(id=id)
    std.delete()
    return redirect('/studentshow')
def update(req,id):
    std = Student.objects.get(id=id)
    if req.method == 'POST':
        form = StudentForm(req.POST,instance=std)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/studentshow/')
    return render(req,'StudentRegistration/update.html',{'std':std})

