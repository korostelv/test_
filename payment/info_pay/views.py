
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView


from .models import Application, Requisit
from django.contrib.auth.models import User

from rest_framework import viewsets
from .serializers import ApplicationSerializer, RequisitSerializer


class ApplicationListView(ListView):
    model = Application
    paginate_by = 100
    template_name = 'application.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def requisits(request):
    object_list = Requisit.objects.all()
    if request.method == 'POST' and 'sorted_val' in request.POST:
        value = request.POST.get('sorted_val')
        if value == 'Типу платежа':
            object_list = Requisit.objects.order_by('type_payment')
        elif value == 'Типу карты':
            object_list = Requisit.objects.order_by('card_type')
        elif value == 'Типу счета':
            object_list = Requisit.objects.order_by('account_type')
        elif value == 'Фамилии':
            object_list = Requisit.objects.order_by('last_name')
        elif value == 'Лимиту':
            object_list = Requisit.objects.order_by('limit')
        else:
            object_list = Requisit.objects.all()
        return render(request, 'index.html', {'object_list': object_list })

    elif request.method == 'POST' and 'search_val' in request.POST and 'search_text' in request.POST:
        search_value = request.POST.get('search_val')
        search_text = request.POST.get('search_text')
        if search_value == 'Типу платежа':
            object_list = Requisit.objects.filter(type_payment=search_text)
        elif search_value == 'Типу карты':
            object_list = Requisit.objects.filter(card_type=search_text)
        elif search_value == 'Типу счета':
            object_list = Requisit.objects.filter(account_type=search_text)
        elif search_value == 'Типу счета':
            object_list = Requisit.objects.filter(account_type=search_text)
        elif search_value == 'Фамилии':
            object_list = Requisit.objects.filter(last_name=search_text)
        elif search_value == 'Лимиту(до)':
            object_list = Requisit.objects.filter(limit__lte=float(search_text))
        return render(request, 'index.html', {'object_list': object_list})

    return render(request, 'index.html', {'object_list': object_list})


class UserListView(ListView):
    model = User
    template_name = 'users.html'


class ShowReqView(DetailView):
    model = Requisit
    template_name = 'show_req.html'


class ApplicationAPIView(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class RequisitAPIView(viewsets.ModelViewSet):
    queryset = Requisit.objects.all()
    serializer_class = RequisitSerializer




