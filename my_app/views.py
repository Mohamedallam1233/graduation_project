from django.shortcuts import render
# Create your views here.
def start_page(request):
    return render(request , 'pages/start_pages.html')
def index(request):
    return render(request , 'pages/index.html')
def app_serves(request):
    return render(request , 'pages/servese.html')
def checkup(request):
    return render(request , 'pages/checkup.html')
def doctor(request):
    return render(request , 'pages/doctor.html')
def nurse(request):
    return render(request , 'pages/nurse.html')
def questionss(request):
    return render(request , 'pages/questionss.html')
def Radiology_Diagnostics(request):
    return render(request , 'pages/Radiology_Diagnostics.html')
