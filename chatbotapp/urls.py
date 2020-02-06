from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'chatbotapp'

urlpatterns = [
    url(r"^messages/$", views.index, name = 'index'),
    url(r"^show/$", views.show, name = 'show'),
]