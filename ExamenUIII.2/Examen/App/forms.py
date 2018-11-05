from django import forms
from .models import Critica

class Criticas(forms.ModelForm):
    CHOICES = (('Buenos ejemplos', 'Buenos ejemplos'),('Urbanismo y vialidad', 'Urbanismo y vialidad'),('Negocios','Negocios'),('Sociales','Sociales'),('Gobierno','Gobierno'),('Servicios a la comunidad y objetos perdidos','Servicios a la comunidad y objetos perdidos'),)
    tema = forms.ChoiceField(choices=CHOICES)
    critica = forms.CharField(widget=forms.Textarea())
    def __init__(self,*args,**kwargs):
        super(Criticas,self).__init__(*args,*kwargs)
        self.fields['tema'].widget.attrs['class']= 'form-control'
        self.fields['critica'].widget.attrs['class'] = 'form-control'
        self.fields['critica'].widget.attrs['placeholder'] = 'Danos tu critica, sin piedad!!!'
    class Meta:
        model = Critica
        fields = ["tema","critica"]