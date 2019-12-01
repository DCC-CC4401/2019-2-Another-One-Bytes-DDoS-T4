from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.urls import reverse_lazy
from users.forms import CustomUserChangeForm, CustomUserCreationForm,changeImage
from django.http import HttpResponseRedirect
from django.contrib import messages

lastActive='perfil'
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



def userProfileAvatar(request):
    if request.method == 'POST':
        form = changeImage(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data.get('foto')
            request.user.set_foto(img)
            request.user.save()
    else:
        form = changeImage()

    return render(request, 'UserProfile-Avatar.html',{'form': form,'active_tab': 'perfil'})

def userProfilePassword(request):

    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Contraseña cambiada correctamente.')
            return redirect('app:userSecurity')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'UserProfile-Password.html',{'form': form,'active_tab': 'seguridad'})

def userProfile(request):

    return render(request, 'UserProfile.html',{'active_tab': 'perfil'})

def userSecurity(request):

    return render(request, 'UserProfile.html', {'active_tab': 'seguridad'})

def userFriends(request):

    return render(request, 'UserProfile.html', {'active_tab': 'amigos'})

def userActivities(request):


    return render(request, 'UserProfile.html',   {'active_tab': 'actividades'})
def register(request):
    pass