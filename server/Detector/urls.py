from django.urls import path
from . import views
from.views import uploadXray

urlpatterns = [
    path('uploadXray/',uploadXray,name = 'uploadXray')
]
