from django.shortcuts import render,redirect
from .forms import CategoryForm
# Create your views here.

def add_category(request):
    if request.method == 'POST':
        add_category = CategoryForm(request.POST)
        if add_category.is_valid:
            add_category.save()
            return redirect('add_category')

    else:
        add_category = CategoryForm()

    return render(request,'add_category.html',{'form': add_category})
