from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import LandingView

urlpatterns = [
    path('admin/', admin.site.urls), 
    path("accounts/", include("django.contrib.auth.urls")),
    path('accounts/', include('accounts.urls')),
    path('tasks/', include('tasks.urls')),
    path('', LandingView.as_view(), name='landing'),

]

handler404 = 'tasks.views.handler404'
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)