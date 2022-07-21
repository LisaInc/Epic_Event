"""epic_event URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from contract.views import ContractViewSet
from user.views import UserViewSet, ClientViewSet
from event.views import EventViewSet

router_contract = routers.DefaultRouter()
router_contract.register("contract", ContractViewSet, basename="contract")

router_user = routers.DefaultRouter()
router_user.register("user", UserViewSet, basename="user")

router_event = routers.DefaultRouter()
router_event.register("event", EventViewSet, basename="event")

router_client = routers.DefaultRouter()
router_client.register("client", ClientViewSet, basename="client")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("rest_framework.urls")),
    path("", include(router_contract.urls)),
    path("", include(router_user.urls)),
    path("", include(router_event.urls)),
    path("", include(router_client.urls)),
]
