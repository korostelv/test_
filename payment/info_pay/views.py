from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from .models import Application, Requisit


class ApplicationListView(ListView):
    model = Application
    paginate_by = 100
    template_name = 'application.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RequisitListView(ListView):
    model = Requisit
    paginate_by = 100
    template_name = 'requisits.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# @csrf_exempt
def sorted_requisites(request):
    if request.method == 'POST':
        value = request.POST.get('sorted_val')
        print(value)
    return HttpResponse("Success")