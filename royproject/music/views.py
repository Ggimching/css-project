from django.shortcuts import render

# Create your views here.
def call(request):
    return render(request, "home.html")