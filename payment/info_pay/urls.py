from django.urls import path
from django.contrib.auth import views as auth_views
from rest_framework import routers

from .views import ApplicationListView, requisits, UserListView, ShowReqView, ApplicationAPIView, RequisitAPIView

app_name = 'info_pay'

router = routers.DefaultRouter()
router.register('api/application', ApplicationAPIView)
router.register('api/requisit', RequisitAPIView)

urlpatterns = [
    path('', requisits, name='requisits'),
    path("application", ApplicationListView.as_view(), name="application"),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('users', UserListView.as_view(), name='users'),
    path('show_req/<int:pk>/', ShowReqView.as_view(), name='show_req'),
    ]

urlpatterns += router.urls