from django.db import models
from datetime import date

class Paciente(models.Model):
    cedula = models.CharField(max_length=11, primary_key=True)
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre 

class Cita(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    cedula = models.ForeignKey(Paciente, on_delete=models.CASCADE)  
    vigencia = models.BooleanField(default=True)
    diacita = models.DateField(default=date.today) 
    horacita = models.TimeField()
    mensaje = models.TextField()
    id_medico = models.ForeignKey('Medico', on_delete=models.CASCADE)  

class Especialidad(models.Model):
    codigoEsp = models.CharField(max_length=10, unique=True) 
    nombreEsp = models.CharField(max_length=100)  

    def __str__(self):
        return self.nombreEsp

class Medico(models.Model):
    codigoMedico = models.CharField(max_length=10, unique=True)  
    nombreMedico = models.CharField(max_length=100)  
    especialidades = models.ManyToManyField(Especialidad, through='EspecialidadMedico')  

    def __str__(self):
        return self.nombreMedico

class EspecialidadMedico(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
