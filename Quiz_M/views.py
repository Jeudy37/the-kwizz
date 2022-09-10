# Create your views here.
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import Quizform
from .models import *
# Create your views here.
def acceuil(request):
    context={}
    return render(request,'acceuil.html',context)



def kreyeKont(request):
    if request.method =='POST':
        nom=request.POST.get('nom')
        modpas=request.POST.get('modpas')
        User.objects.create_user(username=nom, password=modpas)
        return redirect(acceuil)

    return render(request,'kreyekont.html')

def konekte(request):
    if request.method =='POST':
        nom=request.POST.get('nom')
        modpas=request.POST.get('modpas')
        user=authenticate(username=nom ,password=modpas)
        if user is not None:
            login(request,user)
            return redirect(acceuil)
    
    return render(request,'konekte.html')


def kreyekwiz(request):
    form=Quizform()
    if request.method== 'POST':
        form=Quizform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=Quizform()

    context={'form':form}
    return render(request,'kreyekwiz.html',context)

def jwe(request):
    """if request.method == 'POST':"""
    jwet=Quiz.objects.all()
    context={'jwet':jwet}
    return render(request,'jwee.html',context)

"""for a in jwet:
            if a.vre_repons ==request.POST.get(a.question):
                print('ou bon')

            else:
                print('ou pa ok')"""

def krayete(request):
    ote=User.quiz.set.all()
    print(ote)

def dekonekte(request):
    logout(request)
    return redirect(acceuil)