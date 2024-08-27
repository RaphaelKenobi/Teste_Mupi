from django.urls import path
from .views import HomeView, CreateTaskView, DeleteTaskView, ListTaskView, UpdateTaskView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create', CreateTaskView.as_view(), name='create'),
    path('delete/<int:pk>', DeleteTaskView.as_view(), name='delete'),
    path('list', ListTaskView.as_view(), name='list'),
    path('update/<int:pk>', UpdateTaskView.as_view(), name='update'),
]