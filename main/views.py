from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import ModelForm

from .models import Stuff


class StuffForm(ModelForm):
    class Meta:
        model = Stuff
        fields = ('title',)


def index(request):
    stuff = Stuff.objects.all()
    form = StuffForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'main/index.html', {'form': form, 'stuff': stuff})


def delete(request, pk):
    Stuff.objects.filter(id=pk).delete()
    return redirect('index')