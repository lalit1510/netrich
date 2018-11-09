from django.shortcuts import render
from app1.forms import StudentForm
from app1.models import Student
from django.views.generic import TemplateView,ListView,DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

@login_required
def form(request):
    form=StudentForm()
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            pass
    else:
        pass

    return render(request,'form.html',{'form':form})




def login1(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('app1:list'))
        else:
            return HttpResponse("your email or password is incorrect")
    return render(request,'login.html',{})

@login_required
def logout1(request):
    logout(request)
    return HttpResponseRedirect(reverse('app1:index'))












def index(request):
    return  render(request,'index.html',{})


class List(LoginRequiredMixin,ListView):
    model = Student
    template_name = 'list.html'
    paginate_by = 10

class Detail(LoginRequiredMixin,DetailView):
    model = Student
    template_name = 'detail.html'

