from django.shortcuts import render
from django.http import HttpResponse
from . import forms


# Create your views here.
def add_product(request):
    if request.method == "POST":
        form = forms.ProductForm(request.POSt)
        if form.is_valid():
            form.save()
            return HttpResponse('Add Successful')
    else:
        form = forms.ProductForm()
        return render(request, 'form.html', {
            'form': form
        })
