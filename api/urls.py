from django.urls import path

from .views import Form63View

urlpatterns = [
    path('form63/', Form63View.as_view(), name='form63'),
]
