from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ApplicationListView, requisits

app_name = 'info_pay'


urlpatterns = [
    # path('', index, name='index'),
    path('requisits', requisits, name='requisits'),
    path("application", ApplicationListView.as_view(), name="application"),
    # path("requisits/", RequisitListView.as_view(), name="requisits"),
    # path('',LoginView.as_view, name='login'),
    path('', auth_views.LoginView.as_view(), name='login'),
    ]