from django.shortcuts import render


# Create your views here.
def services(request):
    return render(request, 'services.html', {})

def construction(request):
    return render(request, 'construction.html', {})

def mechanics(request):
    return render(request, 'mechanics.html', {})

def logistic(request):
    return render(request, 'logistic.html', {})

def webb(request):
    return render(request, 'webb.html', {})

def law(request):
    return render(request, 'law.html', {})

def other(request):
    return render(request, 'other.html', {})
