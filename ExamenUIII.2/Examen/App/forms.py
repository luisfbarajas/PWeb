from django import forms

class Criticas(forms.Form):
    CHOICES = (('Buenos ejemplos', 'Buenos ejemplos'),('Urbanismo y vialidad', 'Urbanismo y vialidad'),('Negocios','Negocios'),('Sociales','Sociales'),('Gobierno','Gobierno'),('Servicios a la comunidad y objetos perdidos','Servicios a la comunidad y objetos perdidos'),)
    Tema = forms.ChoiceField(choices=CHOICES)
    Critica = forms.CharField(widget=forms.Textarea())
    def __init__(self,*args,**kwargs):
        super(Criticas,self).__init__(*args,*kwargs)
        self.fields['Tema'].widget.attrs['class']= 'form-control'
        self.fields['Critica'].widget.attrs['class'] = 'form-control'
        self.fields['Critica'].widget.attrs['placeholder'] = 'Danos tu critica, sin piedad!!!'