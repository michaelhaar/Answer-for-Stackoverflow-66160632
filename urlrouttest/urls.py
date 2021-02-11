from django.urls import path
from .views import index

app_name = 'urlrouttest'

urlpatterns = [
    path('test-pay-redirect/', index, name='index'),
]
