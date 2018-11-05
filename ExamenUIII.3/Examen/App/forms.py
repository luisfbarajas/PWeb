from django import forms
from .models import RegistroProyecto

class RegistroProyectos(forms.ModelForm):
    name = forms.CharField(label='Nombre del Proyecto:')
    Choices = (('Brenda','Brenda'),('Beatriz','Beatriz'),('Jesus','Jesus'),('Mauricio','Mauricio'),('Ivan','Ivan'))
    lider = forms.ChoiceField(choices=Choices)
    inicia = forms.DateField(widget=forms.DateInput(format="%m/%d/%Y"))
    duracion = forms.IntegerField(label='Duracion(dias):')
    Choices_appoiments = (('semenal','semanal'),('Mensual','Mensual'))
    reuniones = forms.ChoiceField(choices=Choices_appoiments)

    
    def __init__(self, *args, **kwargs):
        super(RegistroProyectos, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class']='form-control'
        self.fields['lider'].widget.attrs['class']='form-control'
        self.fields['inicia'].widget.attrs['class']='form-control'
        self.fields['inicia'].widget.attrs['type']='date'
        self.fields['duracion'].widget.attrs['class']='form-control'
        self.fields['reuniones'].widget.attrs['class']='form-control'

    class Meta:
        model = RegistroProyecto
        fields = ["name","lider","inicia","duracion","reuniones"]
        


