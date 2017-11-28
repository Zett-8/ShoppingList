from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.http import require_POST

from .forms import RegisterForm


@login_required
def index2(request):
    return render(request, 'accounts/login.html')


def new(request):
    form = RegisterForm(request.POST or None)
    content = {'form': form,}
    return render(request, 'accounts/new.html', content)


@require_POST
def create(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('accounts:thankslogin')
    content = {'form': form, }
    return render(request, 'accounts/new.html', content)
