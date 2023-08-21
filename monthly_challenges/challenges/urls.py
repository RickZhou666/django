from django.urls import path

# import from same folder
from . import views

urlpatterns = [
    path("january", views.january), # if request hit "january", execut views.index function
    path("february", views.february) 
]

