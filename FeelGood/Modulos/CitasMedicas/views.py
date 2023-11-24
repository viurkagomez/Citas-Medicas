from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Paciente, Cita, Especialidad, Medico

def FormularioContacto(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Procesa los datos del formulario y crea una instancia de Cita aquí
            # Puedes acceder a los datos del formulario con form.cleaned_data
            # Luego, guarda la cita en la base de datos y redirige a la página de confirmación
            return redirect('pagina_de_confirmacion')  # Cambia 'pagina_de_confirmacion' por la URL deseada
    else:
        form = AppointmentForm()
    
    pacientes = Paciente.objects.all()
    especialidades = Especialidad.objects.all()
    medicos = Medico.objects.all()
    
    return render(request, "formulariocontacto.html", {'form': form, 'pacientes': pacientes, 'especialidades': especialidades, 'medicos': medicos})
