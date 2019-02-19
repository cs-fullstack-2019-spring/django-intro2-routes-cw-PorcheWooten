from django.http import HttpResponse

# sets functions to return whats displayed on the page
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def gogetthegoods(request):
    return HttpResponse("Here you go! Family!")

def happyhappyjoyjoy(request):
    return HttpResponse("Porche' & Paidyn against the world!!")