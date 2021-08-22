from django.urls import path
from . import views


app_name = 'persona_app'

urlpatterns = [
    path(
        '', 
        views.InicioView.as_view(), 
        name='Inicio'
    ),
    path(
        'listar-todo-empleados/', 
        views.ListAllEmpleado.as_view(),
        name = 'listar_empleado'
    ),
    path(
        'lista-by-area/<shorName>/', 
        views.ListByAreaEmpleado.as_view(),
        name= 'empleados_area'
        ),
    path("lista-by-trabajo/<job>/", views.ListByBojEmpleado.as_view()),
    path("buscar-empleado/", views.ListEmpleadosByKword.as_view()),
    path("listar-habilidades-empleado/<id>/", views.ListHabilidadesEmpleado.as_view()),
    path(
        'ver-empleado/<pk>/', 
        views.EmpleadoDetailView.as_view(),
        name='detalle_empleado'
        ),
    path(
        'add-empleado/', 
        views.EmpleadoCreateView.as_view(),
        name='registrar_empleado'    
    ),
    path('success/', views.SuccessView.as_view(), name='correcto'),
    path(
        'update-empleado/<pk>/', 
        views.EmpleadoUpdateView.as_view(), 
        name='modificar_empleado',
    ),
    path(
        'delete-empleado/<pk>/', 
        views.EmpleadoDeleteView.as_view(), 
        name='eliminar_empleado',
    ),
    path(
        'lista-empleado-admin/',
        views.ListAllEmpleadoAdmin.as_view(),
        name = 'lista_empleado_admin'
    )
]
