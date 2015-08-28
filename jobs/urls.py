from django.conf.urls import include, url
from .views import AddView, TaskResultView

urlpatterns = [
    url(r'^add/', AddView.as_view(), name="jobs-add"),
    url(r'taskid/(?P<task_id>.*)/$', TaskResultView.as_view(), name="jobs-result")
    
]