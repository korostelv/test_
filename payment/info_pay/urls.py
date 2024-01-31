from django.urls import path

from .views import ApplicationListView, requisits, index, MyLoginView

app_name = 'info_pay'


urlpatterns = [
    path('', index, name='index'),
    path('requisits', requisits, name='requisits'),
    path("application", ApplicationListView.as_view(), name="application"),
    # path("requisits/", RequisitListView.as_view(), name="requisits"),
    path('',MyLoginView.as_view, name='login')
    ]