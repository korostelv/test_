from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Application, Requisit


class ApplicationListView(ListView):
    model = Application
    paginate_by = 100
    template_name = 'application.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# class RequisitListView(ListView):
#     model = Requisit
#     paginate_by = 50
#     template_name = 'requisits.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context


def requisits(request):
    object_list = Requisit.objects.all()
    if request.method == 'POST':
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
        return render(request, 'requisits.html', {'object_list': object_list })
    return render(request, 'requisits.html', {'object_list': object_list})




