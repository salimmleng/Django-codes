from django.shortcuts import render
from django.http import HttpResponse
from .forms import contactForm,passwordValidation
from .forms import studentData

# Create your views here.

def home(request):
    return render (request,'home.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render (request,'about.html',{'name':name,'email': email,'select':select})
    else: 
        return render (request,'about.html')


def submit_form(request):
    
    return render (request,'form.html')


def djangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST,request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
            return render(request,'django_form.html',{'form': form})
    
    else:
        form = contactForm()
    return render(request,'django_form.html',{'form': form})



def studentForm(request):
    if request.method == 'POST':
        form = studentData(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
        
    else:
        form = studentData()
    return render(request,'django_form.html',{'form': form})


def passwordvalid(request):
    if request.method == 'POST':
        form = passwordValidation(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        
    else:
        form = passwordValidation()
    return render(request,'django_form.html',{'form': form})
