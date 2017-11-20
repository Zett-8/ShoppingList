from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.views import generic
from django.forms import ModelForm

from .models import Stuff


class PostStuff(ModelForm):
    class Meta:
        model = Stuff
        fields = ('title',)


class IndexView(generic.ListView):
    template_name = 'main/index.html'

    def get_queryset(self):
        return Stuff.objects.all()


def index(request):
    form = PostStuff(request.POST)
    stuff = Stuff.objects.all()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('main:index')

    return render(request, 'main/index.html', {'form': form, 'stuff': stuff})