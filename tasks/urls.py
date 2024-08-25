from django.urls import path
from .views import HomeView, CreateView, DeleteView, ListView, UpdateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create', CreateView.as_view(), name='create'),
    path('delete', DeleteView.as_view(), name='delete'),
    path('list', ListView.as_view(), name='list'),
    path('update', UpdateView.as_view(), name='update'),


]