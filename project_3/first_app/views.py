from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def home(request):
    d = {'Author': 'Salim', 'age': 5,'lst': ['python','is','best'],
         'birthday': datetime.datetime.now(),'val': ['salim','almina','rana'],
           'courses': [
        {
            'id' : 1,
            'name': 'python',
            'fee' : 5000
        },
        {
            'id' : 2,
            'name': 'Django',
            'fee' : 8000
        },
        {
            'id' : 3,
            'name': 'C',
            'fee' : 2000
        },
    ]}
    return render(request,"first_app/home.html",d)
