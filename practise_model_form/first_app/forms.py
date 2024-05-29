from django import forms 

from .models import StudentModel

class StudentForm(forms.ModelForm):

    class Meta:
        model = StudentModel
        fields = '__all__'
        labels = {
            'name' : 'Student name',
            'roll': 'Student roll',
        }

        help_texts = {
            'name' : 'Write your full name',
            'mother_name': 'Write your mother name',
        }

