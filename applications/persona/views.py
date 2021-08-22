from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
from .models import Empleado
from .forms import EmpleadoForm

# Create your views here.
class InicioView(TemplateView):
    template_name = 'inicio.html'
    

class ListAllEmpleado(ListView):
    template_name = 'persona/list_all.html'
    # model = Empleado
    paginate_by = 4
    ordering = '-id'
    def get_queryset(self):
        nombre_completo = self.request.GET.get('nombre_completo','')
        print(nombre_completo)
        lista = Empleado.objects.filter(
            full_name__icontains=nombre_completo
        )
        return lista


class ListAllEmpleadoAdmin(ListView):
    template_name = 'persona/lista_empleados_admin.html'
    paginate_by = 10
    ordering = '-id'
    context_object_name = 'empleados'
    model = Empleado


# Listar empleados por el area
class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'
    def get_queryset(self):
        shor_name = self.kwargs['shorName']
        lista = Empleado.objects.filter (
            departamento__shor_name = shor_name
        )
        return lista


# Listar empleados por trabajo
class ListByBojEmpleado(ListView):
    template_name = 'persona/list_by_trabajo.html'
    model = Empleado
    def get_queryset(self):
        job = self.kwargs['job']
        job_id = -1
        for elemento in Empleado.job_choices:
            if elemento[1].lower().find(job.lower()) >= 0:
                job_id = elemento[0]

        lista = Empleado.objects.filter(
            job = job_id
        )
        return lista 


class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        
        palabra_clave = self.request.GET.get('kword_xd_name','')
        print('**************************')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        print(lista)
        return lista


class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name ='habilidades'
    def get_queryset(self):
        id = self.kwargs['id']
        print(id)
        empleado = Empleado.objects.get(id=id)
        print(empleado)
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    template_name = 'persona/detail_empleado.html'
    model = Empleado
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['texto'] = 'Este es el texto de detailView'
        return context


class SuccessView(TemplateView):
    template_name = 'persona/success.html'


class EmpleadoCreateView(CreateView):
    template_name = 'persona/add.html'
    
    form_class = EmpleadoForm

    success_url = reverse_lazy('persona_app:lista_empleado_admin')

    def form_valid(self, form):
        # Lógica del proceso
        empleado = form.save(commit=False)
        empleado.full_name = f'{empleado.first_name} {empleado.last_name}'
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = 'persona/update.html'
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'hoja_vida',
    ]
    success_url = reverse_lazy('persona_app:lista_empleado_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('*****************METODO POST*****************')
        print('**********************************')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)


    def form_valid(self, form):
        print('*****************METODO FORM VALID*****************')
        print('**********************************')
        return super().form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'persona/delete.html'
    success_url = reverse_lazy('persona_app:correcto')