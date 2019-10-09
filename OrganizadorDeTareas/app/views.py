from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'LandingPage.html')

def userProfile(request):
    return render(request, 'UserProfile.html')
