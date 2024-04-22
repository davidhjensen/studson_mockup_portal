from django.http import HttpResponse

def home(request):
    return HttpResponse("tony is awesome!")