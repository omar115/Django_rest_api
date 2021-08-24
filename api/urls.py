from django.conf.urls import url 
from django.urls import path
from .views import *

urlpatterns = [
    path('status/v1/', StatusAPIView.as_view()),
    path('status/v2/', StatusListApiView.as_view()),    # to see all status list
    path('status/create/', StatusCreateApiView.as_view()),  # to create a new status
    path('status/v2/detail/<id>/', StatusDetailApiView.as_view()),  # to see single status detail
    path('status/v2/detail/update/<id>/', StatusUpdateApiView.as_view()),   # to update one status
    path('status/v2/delete/<id>/', StatusDeleteApiView.as_view()),  # to delete a single status
]