from django import forms 
from django.core import validators

# widget 
class contactForm(forms.Form):
    name = forms.CharField(label = "Full Name: ",initial="salim",
     help_text="Total length must be 30 charecters",required=False,
       widget=forms.Textarea(attrs= {'id': 'text_area','class':
         'class1 class2','placeholder': 'Enter your name'}))


    # file = forms.FileField() 


    # email = forms.EmailField(label = "User email")
    # age = forms.IntegerField()
    # weight = forms.FloatField()

    age = forms.CharField(widget= forms.NumberInput)
    balance = forms.DecimalField()
    check = forms.BooleanField()
    birthday = forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    CHOICES = [('S','small'),('M','medium'),('L','large')]
    size  = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)

    meal = [('p','peperoni'),('M','Masroom'),('B','beef')]

    pizza = forms.MultipleChoiceField(choices=meal, widget=forms.CheckboxSelectMultiple)


# class studentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)

#     def clean(self):
#       cleaned_data = super().clean()
#       valname = self.cleaned_data['name']
#       valemail = self.cleaned_data['email']
#       if len(valname) < 10:
#          raise forms.ValidationError('Enter a name at least 10 charecters')
#       if '.com' not in valemail:
#          raise forms.ValidationError("Your email must contain .com")

# nijer toiri function o validator diye pass kora jabe

def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter at least 10 chars")

class studentData(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10,message 
    = "Enter a name at most 10 character")])
    text = forms.CharField(widget=forms.TextInput,validators=[len_check])

    email = forms.CharField(widget=forms.EmailInput, 
    validators=[validators.EmailValidator(message='Enter a valid email')])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34,message="Age must be at most 34"),validators.MinValueValidator(24,message='Age must be at least 24')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'],message='file must be pdf and png ')])


class passwordValidation(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']

        if val_pass != val_conpass:
            raise forms.ValidationError("Password doesn't match")

