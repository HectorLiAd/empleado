from django.urls import path
from . import views

urlpatterns = [
    path('prueba/', views.PruebaView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.ListarPrueba.as_view()),
    path('add/', views.PruebaCreateView.as_view()),
    path(
        'resumen-foundation/',
        views.ResumenFoundationView.as_view(),
        name='resumen_foundation'
        )
]