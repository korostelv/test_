from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ApplicationListView, requisits, UserListView, ShowReqView, ApplicationAPIView, RequisitAPIView

# from rest_framework import routers
# from .api import ApplicationViewSet, RequisitViewSet
#
# router = routers.DefaultRouter()
# router.register('api/application', ApplicationViewSet, 'application')
# router.register('api/requisit', RequisitViewSet, 'requisit')

app_name = 'info_pay'


urlpatterns = [
    path('', requisits, name='requisits'),
    path("application", ApplicationListView.as_view(), name="application"),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('users', UserListView.as_view(), name='users'),
    path('show_req/<int:pk>/', ShowReqView.as_view(), name='show_req'),
    path('api/application/', ApplicationAPIView.as_view()),
    path('api/requisit/', RequisitAPIView.as_view()),
    ]