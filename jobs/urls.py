from django.conf.urls import include, url
from .views import AddView

urlpatterns = [
    url(r'^add/', AddView.as_view(), name="add-view")
    
]