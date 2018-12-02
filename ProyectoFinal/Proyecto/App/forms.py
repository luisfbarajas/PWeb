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
