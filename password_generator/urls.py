from django.contrib import admin
from django.urls import path, include

# This includes the app's URLs in the main project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('password_app.urls')),
]
