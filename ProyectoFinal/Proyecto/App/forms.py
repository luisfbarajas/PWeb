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
    ProyectName = forms.CharField()
    EnterpriseName = forms.CharField()
    represent = forms.CharField()
    deparment = forms.ChoiceField(choices = deparment_choices)
    start = forms.DateField(widget=forms.DateInput(format="%m/%d/%Y"))
    ends = forms.DateField(widget=forms.DateInput(format="%m/%d/%Y"))
    description = forms.CharField(widget=forms.Textarea())
    generalObj = forms.CharField()
    vision = forms.CharField(widget=forms.Textarea())
    # administratos = forms.CharField()
    def __init__(self, *args, **kwargs):
        super(RegistroProyecto, self).__init__(*args, **kwargs)
        self.fields['ProyectName'].widget.attrs['class']='form-control'
        self.fields['EnterpriseName'].widget.attrs['class']='form-control'
        self.fields['represent'].widget.attrs['class']='form-control'
        self.fields['deparment'].widget.attrs['class']='form-control'
        self.fields['start'].widget.attrs['class']='form-control'
        self.fields['ends'].widget.attrs['class']='form-control'
        self.fields['description'].widget.attrs['class']='form-control'
        self.fields['generalObj'].widget.attrs['class']='form-control'
        self.fields['vision'].widget.attrs['class']='form-control'
    class Meta:
        model = models_DB.RegistroProyecto
        fields = [
            "NombreProyecto",
            "NombreEmpresa",
            "representante",
            "departamento",
            "inicia",
            "finaliza",
            "descripcion",
            "ObjGeneral",
            "vision"]
