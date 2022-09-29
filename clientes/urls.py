from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes, name="clientes"),
    path('atualiza_cliente/', views.att_cliente, name="atualiza_cliente"),
    path('excluir_carro/<int:id>', views.excluir_carro, name="excluir_carro"),
    path('update_carro/<int:id>', views.update_carro, name="update_carro"),
    path('update_cliente/<int:id>', views.update_cliente, name="update_cliente")
]