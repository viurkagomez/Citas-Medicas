from django.contrib import admin
from .models import Paciente, Cita, Medico, Especialidad, EspecialidadMedico

# Registrar el modelo Paciente
admin.site.register(Paciente)

# Registrar el modelo Cita con un campo para buscar por cédula de paciente y médico
class CitaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'cedula', 'id_medico', 'vigencia', 'diacita', 'horacita')
    list_filter = ('vigencia', 'diacita')
    search_fields = ('codigo', 'cedula__nombre', 'id_medico__nombre')
admin.site.register(Cita, CitaAdmin)

# Registrar el modelo Medico
admin.site.register(Medico)

# Registrar el modelo Especialidad
admin.site.register(Especialidad)

# Registrar el modelo EspecialidadMedico
admin.site.register(EspecialidadMedico)
