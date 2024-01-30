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


class RequisitListView(ListView):
    model = Requisit
    paginate_by = 100
    template_name = 'requisits.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context