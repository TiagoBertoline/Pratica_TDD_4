from django.urls import path
from core.views import login, logout, home
from . import views


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('index/', home, name='index'),
    path('', home,name='home'),
    #  Outras urls.
    path('contatos/', views.listar_contatos, name='listar_contatos'),
    path('cadastrar/', views.cadastrar_contato, name='cadastrar_contato'),
    path('atualizar/<int:id>/', views.atualizar_contato, name='atualizar_contato'),
    path('remover/<int:id>/', views.remover_contato, name='remover_contato'),
]