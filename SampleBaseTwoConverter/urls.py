from django.contrib import admin
from django.urls import path
from main.views import index
from main.views import convert


urlpatterns = [
    path('', index),
    path('convert/', convert),
    path('admin/', admin.site.urls),
]
