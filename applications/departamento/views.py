from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import NewDepartamentoForm
from applications.persona.models import Empleado
from applications.departamento.models import Departamento

class ListaDepartamentoListView(ListView):
    template_name = 'departamento/lista.html'
    context_object_name = 'departamentos'
    model = Departamento

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        print('Estamos en el form valid')

        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        departamento = form.cleaned_data['departamento']
        shortname = form.cleaned_data['shortname']

        depa = Departamento(
            name = departamento,
            shor_name = shortname,
        )
        depa.save()

        Empleado.objects.create(
            first_name = nombre,
            last_name = apellidos,
            full_name = f'{nombre} {apellidos}',
            job = '1',
            departamento = depa,
            hoja_vida = '123'
        )
        return super(NewDepartamentoView, self).form_valid(form)  
