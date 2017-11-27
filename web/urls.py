from django.conf.urls import url, include

from .views import *


urlpatterns = [
    url(r'^(?P<pk>\d+)/', help_im_pay),
    url(r'^create', create_help_im_pay)
]


