from django.shortcuts import render
from .models import Page
from django.urls import reverse_lazy
from django.views.generic import ListView , DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView 
    )



# Create your views here.
class PagesHomePage(ListView):
    model = Page
    template_name = "home.html"


class PagesMusic(ListView):
    model = Page
    template_name = "music.html"


class PagesMusicDetail(DetailView):
    model = Page
    template_name = "music_detail.html"

class PagesPotato(ListView):
    model = Page
    template_name = "music_potato.html"

class PagesCreateMusic(CreateView):
    model = Page
    template_name = "music_new.html"
    fields = ['title', 'lyrics', 'video_url', 'user']


class PagesUpdateMusic(UpdateView):
    model = Page
    template_name = "music_edit.html"
    fields = ['title', 'lyrics', 'video_url', 'user']

class PageDeleteMusic(DeleteView):
    model = Page
    template_name = "music_delete.html"
    success_url = reverse_lazy("home")