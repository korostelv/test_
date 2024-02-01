from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ApplicationListView, requisits, UserListView

app_name = 'info_pay'


urlpatterns = [
    path('requisits', requisits, name='requisits'),
    path("application", ApplicationListView.as_view(), name="application"),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('users', UserListView.as_view(), name='users'),
    ]