from django.urls import path
from . import views

# essas são as urls de cada views
urlpatterns = [
 path('', views.lista_livros, name='lista_livros'),
 path('criar/', views.item_creat, name='item_creat'),
 path('atulizar/<int:pk>', views.item_update, name='item_update'),
 path('delete/<int:pk>', views.item_delete, name='item_delete'),
]