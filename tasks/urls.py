from django.urls import path
from .views import HomeView, CreateTaskView, DeleteTaskView, ListTaskView, UpdateTaskView, complete_task
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('home', login_required(HomeView.as_view()), name='home'),
    path('create', login_required(CreateTaskView.as_view()), name='create'),
    path('delete/<int:pk>', login_required(DeleteTaskView.as_view()), name='delete'),
    path('list', login_required(ListTaskView.as_view()), name='list'),
    path('update/<int:pk>', login_required(UpdateTaskView.as_view()), name='update'),
    path('complete/<int:pk>', login_required(complete_task), name='complete_task'),
]
