from django.urls import path
from .views import LoginView, HomeView, CreateTaskView, DeleteTaskView, ListTaskView, UpdateTaskView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('home', HomeView.as_view(), name='home'),
    path('create', CreateTaskView.as_view(), name='create'),
    path('delete/<int:pk>', DeleteTaskView.as_view(), name='delete'),
    path('list', ListTaskView.as_view(), name='list'),
    path('update/<int:pk>', UpdateTaskView.as_view(), name='update'),
]