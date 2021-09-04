from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
    'variable1': "Harry",
    'variable2': "Sam"
    }
    return render(request, 'index.html', context)
   #return HttpResponse("This is homeApp page")

def about(request):
    return HttpResponse("This is about page")

def services(request):
    return HttpResponse("This is service page")

def contact(request):
    return HttpResponse("This is contact page")