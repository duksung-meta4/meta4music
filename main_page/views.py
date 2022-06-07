from django.shortcuts import render

# Create your views here.
def home(requests):
    return render(requests, 'home.html')

def drawing(requests):
    return render(requests, 'drawing.html')


def playing(requests):
    return render(requests, 'playing.html')