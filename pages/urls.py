from django.urls import path

from .views import PagesHomePage
from .views import PagesMusic 
from .views import PagesMusicDetail, PagesCreateMusic, PagesUpdateMusic, PageDeleteMusic, PagesPotato


urlpatterns = [
    path("", PagesHomePage.as_view(), name="home"),
    path("music/", PagesMusic.as_view(), name="music"),
    path("music/<int:pk>", PagesMusicDetail.as_view(), name="music_detail"),
    path("potato/", PagesPotato.as_view(), name="potato"),
    path("music/<int:pk>/edit/", PagesUpdateMusic.as_view(), name="music_edit"),
    path("music/new", PagesCreateMusic.as_view(), name="music_new"),
    path("music/<int:pk>/delete/", PageDeleteMusic.as_view(), name="music_delete")
]