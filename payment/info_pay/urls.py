from django.urls import path

from .views import ApplicationListView, RequisitListView, sorted_requisites

app_name = 'app_name'


urlpatterns = [
    # path('', index, name='index'),
    path("", ApplicationListView.as_view(), name="application"),
    path("requisits/", RequisitListView.as_view(), name="requisits"),
    path('sorted_requisites', sorted_requisites, name='sorted_requisites'),
    ]