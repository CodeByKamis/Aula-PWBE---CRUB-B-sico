from django.urls import path
from . import views #o ponto serve para indicar que é da pasta local ou seja mesma pasta

urlpatterns = [
    path('', views.item_read, name='item_read'),
    path('bruno/', views.item_creat, name='item_creat'),
    path('giovana/<int:pk>', views.item_update, name = "item_update"),
    path('luana/<int:pk>', views.item_delete, name='item_delete')
]