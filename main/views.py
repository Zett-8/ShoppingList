
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.forms import ModelForm

from .models import Stuff


class StuffForm(ModelForm):
    class Meta:
        model = Stuff
        fields = ('title',)


def index(request):
    if request.user.is_active:
        stuff = Stuff.objects.filter(user=request.user)
        form = StuffForm(request.POST)
        if request.method == "POST":
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.save()
                return redirect('main:index')

        return render(request, 'main/index.html', {'form': form, 'stuff': stuff})
    else:
        return render(request, 'main/welcome.html')


def delete(request, pk):
    Stuff.objects.filter(id=pk).delete()
    return redirect('main:index')


def deleteall(request):
    Stuff.objects.filter(user=request.user).delete()
    return redirect('main:index')
