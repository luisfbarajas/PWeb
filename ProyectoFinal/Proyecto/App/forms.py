from django import forms
from . import models as models_DB

class RegistroProyecto(forms.ModelForm):
    deparment_choices = (
        ('Recursos Humanos','Recursos Humanos'),
        ('Desarrollo', 'Desarrollo'),
        ('Contabilidad','Contabilidad'),
        ('Produccion','Produccion'),
        ('Calidad','Calidad')
        )
    NombreProyecto = forms.CharField()
    Cliente = forms.CharField()
    representante = forms.CharField()
    departamento = forms.ChoiceField(choices = deparment_choices)
    inicia = forms.DateField(widget=forms.DateInput(format="%m/%d/%Y"))
    finaliza = forms.DateField(widget=forms.DateInput(format="%m/%d/%Y"))
    descripcion = forms.CharField(widget=forms.Textarea())
    ObjGeneral = forms.CharField()
    def __init__(self, *args, **kwargs):
        super(RegistroProyecto, self).__init__(*args, **kwargs)
        self.fields['NombreProyecto'].widget.attrs['class']='form-control'
        self.fields['NombreProyecto'].widget.attrs['placeholder']='Nombre del proyecto'
        self.fields['Cliente'].widget.attrs['class']='form-control'
        self.fields['Cliente'].widget.attrs['placeholder']='Nombre de la empresa'
        self.fields['representante'].widget.attrs['class']='form-control'
        self.fields['representante'].widget.attrs['placeholder']='Representante'
        self.fields['departamento'].widget.attrs['class']='form-control'
        self.fields['inicia'].widget.attrs['class']='form-control'
        self.fields['finaliza'].widget.attrs['class']='form-control'
        self.fields['descripcion'].widget.attrs['class']='form-control'
        self.fields['descripcion'].widget.attrs['placeholder']='Descripcion'
        self.fields['ObjGeneral'].widget.attrs['class']='form-control'
        self.fields['ObjGeneral'].widget.attrs['placeholder']='Objetivo'

    class Meta:
        model = models_DB.RegistroProyecto
        fields = [
            "NombreProyecto",
            "Cliente",
            "representante",
            "departamento",
            "inicia",
            "finaliza",
            "descripcion",
            "ObjGeneral"]


class addActivitiForm(forms.ModelForm):
    actividad_tipo =  (
        ('Individual','Individual'),
        ('Multiple','Multiple'))

    estado_tipo = (
         ('Pendiente','Pendiente'),
         ('Asignada','Asignada'),
         ('Cancelada','Cancelada'))
    actividadName = forms.CharField()
    type = forms.ChoiceField(choices = actividad_tipo)
    estado = forms.ChoiceField( choices = estado_tipo)
    inicia = forms.DateField()
    finaliza = forms.DateField()
    encargado = forms.ModelChoiceField(queryset = models_DB.empleados.objects.all())
    proyecto = forms.ModelChoiceField(queryset = models_DB.RegistroProyecto.objects.all())

    def __init__(self, *args, **kwargs):
        super(addActivitiForm,self).__init__(*args,**kwargs)
        self.fields['actividadName'].widget.attrs['class'] = 'form-control'
        self.fields['actividadName'].widget.attrs['placeholder'] = 'Nombre de actividad'
        self.fields['type'].widget.attrs['class'] = 'form-control'
        self.fields['estado'].widget.attrs['class'] = 'form-control'
        self.fields['inicia'].widget.attrs['class']= 'form-control'
        self.fields['finaliza'].widget.attrs['class'] = 'form-control'
        self.fields['encargado'].widget.attrs['class'] = 'form-control'
        self.fields['proyecto'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = models_DB.Actividades
        fields = (
            'actividadName',
            'type',
            'estado',
            'inicia',
            'finaliza',
            'proyecto',
        )