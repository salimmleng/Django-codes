from django.shortcuts import render
from .forms import CategoryForm
# Create your views here.
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = CategoryForm()
    return render(request, 'add_category.html',{'form':form})