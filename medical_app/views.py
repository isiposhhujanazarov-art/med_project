from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def contacts_view(request):
    return render(request, 'contacts.html')

def location_view(request):
    return render(request, 'location.html')

def services_view(request):
    return render(request, 'services.html')

def doctors_view(request):
    return render(request, 'doctors.html')