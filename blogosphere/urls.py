
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
