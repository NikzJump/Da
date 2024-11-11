from django.urls import path
from . import views


urlpatterns = [
    path('get_war_prod/<int:pk>', views.get_warehouse_products),
    path('get_group_prod/<int:pk>', views.get_group_products),
    path('get_prod/<int:pk>', views.get_prod),
]
