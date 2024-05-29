from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.



def practise_page(request):
    number_list = [1,2,3,4,5,6,7]
    context = {
        'list': ['a','b','c','d'],
        'val': number_list,
        'add': 4,
        'slash': "I'm salim",
        'cap': 'this is salim',
        'cen': 'salim',
        'cut': 'My name is salim',
        'birthday': datetime.datetime.now(),
        'def':"",
        'sort':[
            {'name': 'Josh', 'age': 19},
            {'name': 'Dave', 'age': 22},
            {'name': 'Joe', 'age': 31},
        ],
        'div': 22,
        'value': 102425487,
        'f_item': ['salim','almina','korim'],

        'las':['a','b','c','d'],
        'join':['a','b','c'],

        'line_num':'cat\ndog\nhorse',

        'low': 'Django is best',
        'up': 'python is also best',
        'makeList':'1234',
        'ran': ['a','b','c','d'],

        'some_list': ['a','b','c','d'],

        'slug': 'Jai is a slug',
        'tme': datetime.datetime.now(),
        't': 'my First poSt',

        'cnt': 'jai is a slug ',
        'trun': 'Happy coding',
        'word': 'Django is a best course',
        'strip': '<b>I</b> <button>love</button> <span>dogs</span>',
        'mybirthdate': datetime.datetime(1996, 12, 31),   
        'mydate': datetime.datetime.now(),
        

    }

    
    return render(request,'first_app/practise_page.html',context)
