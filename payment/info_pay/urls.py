from django.urls import path

from .views import ApplicationListView, requisits

app_name = 'info_pay'


urlpatterns = [
    # path('', index, name='index'),
    path('requisits', requisits, name='requisits'),
    path("", ApplicationListView.as_view(), name="application"),
    # path("requisits/", RequisitListView.as_view(), name="requisits"),
    ]