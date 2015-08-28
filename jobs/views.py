from django.shortcuts import render
from django.views.generic import TemplateView
from celery.result import AsyncResult

from .tasks import add


class AddView(TemplateView):
    template_name = "jobs/add.html"
    
    def get_context_data(self, **kwargs):
        context = super(AddView, self).get_context_data(**kwargs)
        task = add.delay(2, 2)
        context['task_id'] = task.task_id

        return context


class TaskResultView(TemplateView):
    template_name= "jobs/taskid.html"
    
    def get_context_data(self, **kwargs):
        context = super(TaskResultView, self).get_context_data(**kwargs)
        task_id = kwargs['task_id']
        async_res = AsyncResult(task_id)
        context['result'] = async_res.get()
        context['task_id'] = task_id
        return context