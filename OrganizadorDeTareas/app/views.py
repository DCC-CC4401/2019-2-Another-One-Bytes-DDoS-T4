from django.shortcuts import render, HttpResponse

# Create your views here.
def login(request):
    return render(request, 'Unlogged.html')

def register(request):
    return render(request, 'Registro.html')

def index(request):
    return render(request, 'LandingPage.html')

def userProfile(request):
    return render(request, 'UserProfile.html', {'active_tab': 'perfil'})

def userSecurity(request):
    return render(request, 'UserProfile.html', {'active_tab': 'seguridad'})

def userFriends(request):
    return render(request, 'UserProfile.html', {'active_tab': 'amigos'})

def userActivities(request):
    return render(request, 'UserProfile.html',   {'active_tab': 'actividades'})
