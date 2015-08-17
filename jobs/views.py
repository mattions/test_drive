from django.shortcuts import render
from django.views.generic import TemplateView
from celery.result import AsyncResult

from .tasks import add


class AddView(TemplateView):
    template_name = "job/add.html"
    
    def get_context_data(self, **kwargs):
        context = super(AddView, self).get_context_data(**kwargs)
        task_id = add.delay(2, 2)
        result = AsyncResult(task_id)
        context['res'] = result.get()
        return context