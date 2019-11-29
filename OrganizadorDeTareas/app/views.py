from django.shortcuts import render, HttpResponse
from users.forms import CustomUserChangeForm, CustomAutenticationForm, CustomUserCreationForm
from django.http import HttpResponseRedirect


# Create your views here.
def login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CustomAutenticationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomAutenticationForm()

    return render(request, 'Unlogged.html', {'form': form})

def registerPage(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CustomUserCreationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomUserCreationForm()

    return render(request, 'Registro.html', {'form': form})

def landing(request):
    return render(request, 'LandingPage.html')

def test(request):
    return render(request, 'test.html')

def index(request):
    return render(request, 'index.html')

def userProfile(request):
    return render(request, 'UserProfile.html', {'active_tab': 'perfil'})

def userSecurity(request):
    return render(request, 'UserProfile.html', {'active_tab': 'seguridad'})

def userFriends(request):
    return render(request, 'UserProfile.html', {'active_tab': 'amigos'})

def userActivities(request):
    return render(request, 'UserProfile.html',   {'active_tab': 'actividades'})
def register(request):
    pass