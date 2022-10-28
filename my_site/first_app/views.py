from urllib import request
from django.shortcuts import render

# Create your views here.


def example_view(request):
    #first_app/templates/first_app/example.html
    return render(request,'first_app/example.html')

def variable_view(request):
    return render(request, 'first_app/variable.html')