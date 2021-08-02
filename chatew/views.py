from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib.auth.models import User
def home(request):
    return render(request,'chat.html')
def create(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
      
        if form.is_valid():
            user=form.save()
            name=form.cleaned_data['username']
            passs=form.cleaned_data['password1']
           
            user=authenticate(request,username=name,password=passs)
            if user is not None:
                login(request,user)
           
            
  
                return redirect('home')
            
          
          
  
     
    context={'form':form}
    
    return render(request, 'signup.html',context)
def logoutuser(request):
    logout(request)
    return redirect('login')
def signin(request):
     if request.method=='POST':
         name=request.POST.get('name')
         passs=request.POST.get('pass')
         user=authenticate(request,username=name,password=passs)
         if user is not None:
             login(request,user)
             
             
             return redirect('home')
    
     return render(request,'signin.html')
