from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from users.forms import CustomUserChangeForm, CustomUserCreationForm,changeImage
from django.http import HttpResponseRedirect


# Create your views here.
def loginPage(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AuthenticationForm(data=request.POST)
        # check whether it's valid:
        if form.is_valid():

            login(request, form.user_cache)
            return redirect('/landing')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = AuthenticationForm()

    return render(request, 'Unlogged.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'index.html')


def registerPage(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CustomUserCreationForm(request.POST,request.FILES)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            pic=form.cleaned_data.get('foto')
            correo = form.cleaned_data.get('correo')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(correo=correo, password=raw_password)
            login(request, user)
            return redirect('/landing')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomUserCreationForm()

    return render(request, 'Registro.html', {'form': form})

def landing(request):
    return render(request, 'LandingPage.html')



def index(request):
    return render(request, 'index.html')

def userProfile(request):
    if request.method == 'POST' and 'submit_foto' in request.POST:
        form=changeImage(request.POST,request.FILES)
        if form.is_valid():
            request.user.set_foto(request.FILES)
            request.user.save()
    else:
        form = changeImage()


    return render(request, 'UserProfile.html', {'form': form,'active_tab': 'perfil'})

def userSecurity(request):
    return render(request, 'UserProfile.html', {'active_tab': 'seguridad'})

def userFriends(request):
    return render(request, 'UserProfile.html', {'active_tab': 'amigos'})

def userActivities(request):
    return render(request, 'UserProfile.html',   {'active_tab': 'actividades'})
def register(request):
    pass