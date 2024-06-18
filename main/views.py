from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls.base import reverse
from account.models import User


def index(request):
    """
    Render the main page
    """
    #    return render(request, 'main/main.html', {})

    context = {'like': 'Django 很棒 Django 很棒 Django 很棒'}
    return render(request, 'main/main.html', context)


def main(request):
    """
    Render the main page
    """
    context = {'like': 'Django 很棒'}
    return render(request, 'main/main.html', context)


def about(request):
    """
    Render the about page
    """
    return render(request, 'main/about.html')


def bike(request):
    """
    Render the bike page
    """
    return render(request, 'main/bike.html')

def csstest(request):
    """
    Render the bike page
    """
    return render(request, 'main/csstest.html')



def django(request):
    """
    Render the bike page
    """
    return render(request, 'main/django.html')


def admin_required(func):
    def auth(request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, '請以管理者身份登入')
            return redirect(reverse('account:login') + '?next=' + request.get_full_path())
        return func(request, *args, **kwargs)

    return auth


def users(request):
    users = User.objects.all()
    return render(request, 'main/users.html', {'users': users})
