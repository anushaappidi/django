from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is Home Page")
def about(request):
    return HttpResponse("ABOUT")
def service(request):
    return HttpResponse("Services")
