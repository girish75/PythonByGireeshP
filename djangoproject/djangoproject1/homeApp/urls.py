"""djangoproject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
This is Application = SRC - urls.py
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name='homeApp'),
    path("about", views.about, name='about'),
    path("services", views.about, name='services'),
    path("contact", views.about, name='contact'),
    ]


