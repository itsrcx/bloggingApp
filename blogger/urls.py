from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.Home, name='home'),
    path('post/',views.Post, name='post'),
    path('about/',views.About, name='about'),
    path('contact/',views.Contact, name='contact'),
]
