from django import forms 

from .models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels={
            'name': 'student name',
            'roll': 'student roll',

        }
       

        help_texts ={
            'name' : 'write your full name',
        }

