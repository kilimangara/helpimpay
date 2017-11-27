from django.conf.urls import url, include

from .views import *


urlpatterns = [
    url(r'^helpimpay/(?P<pk>\d+)', help_im_pay),
    url(r'^helpimpay/create', create_help_im_pay)
]


