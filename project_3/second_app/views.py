from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'second_app/home3.html')

def practise(request):

    d = {'Author': 'Salim','age': 27, 'profession': 'student','courses': [
        {
            'id': 1,
            'course_name': 'Python',
            'fee': 10000
        },
        {
            'id': 2,
            'course_name': 'Django',
            'fee': 12000
        },
        {
            'id': 3,
            'course_name': 'Algo',
            'fee': 8000
        },
    ]}
     

    return render (request,'second_app/practise.html',d)