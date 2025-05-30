from django.shortcuts import render

# Create your views here.


def dashboard(request):
    templates = 'dashboard.html'
    return render(request, templates)
