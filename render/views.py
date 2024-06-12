from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'render/index.html', {})


def bike(request):
    """
    Render the bike page
    """
    return render(request, 'render/bike.html')


def main(request):
    """
    Render the main page
    """
    context = {'like': 'Django 很棒'}
    return render(request, 'main/main.html', context)

