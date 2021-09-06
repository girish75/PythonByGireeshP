from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.views.generic import RedirectView

urlpatterns = [
    path("", views.challenges_home), #/challenges/
    path( "<int:month>", views.monthly_challenge_bynumber ), # int works before STR else it will not work.
    path("<str:month>", views.monthly_challenge, name = "str_path_identifier"),
   ]

