from django.conf.urls import url
from django.db.models import base 
from django.urls import path
from rest_framework import routers
from .views import *

# for viewset you must use router
from rest_framework.routers import DefaultRouter

# if you use router and viewset together, basically for viewset you 
# need to use router. then you can just create one url, and the router
# will generate automically all links for you to do CRUD operation

router = DefaultRouter()
router.register(r'status', StatusViewSet, basename="status")
urlpatterns = [] + router.urls


# urlpatterns = [
#     path('status/v1/', StatusAPIView.as_view()),
#     path('status/v2/', StatusListApiView.as_view()),    # to see all status list
#     path('status/create/', StatusCreateApiView.as_view()),  # to create a new status
#     path('status/v2/detail/<id>/', StatusDetailApiView.as_view()),  # to see single status detail
#     path('status/v2/detail/update/<id>/', StatusUpdateApiView.as_view()),   # to update one status
#     path('status/v2/delete/<id>/', StatusDeleteApiView.as_view()),  # to delete a single status

#     # how to optimize using less api urls in mixins
#     path('status/v3/', StatusListCreateView.as_view()), # to get and post using mixin
#     path('status/<id>/', StatusUpdateDeleteApiView.as_view()),    # to update and delete using mixin
# ]