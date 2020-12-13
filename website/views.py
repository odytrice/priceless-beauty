from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'website/index.html')

def skincare(request):
    return render(request, 'website/skincare.html')

def makeup(request):
    return render(request, 'website/makeup.html')

def hair(request):
    return render(request, 'website/hair.html')