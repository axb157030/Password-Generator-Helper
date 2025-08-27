from django.urls import path
from . import views

# This connects the view to a URL
# This file maps URL paths to view functions.
# When a user visits '/', Django calls views.index.
urlpatterns = [
    path('', views.index, name='index'),
]
