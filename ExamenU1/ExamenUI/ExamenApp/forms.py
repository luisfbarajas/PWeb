from django import forms
from .models import Player

class PlayerForm(forms.Form):
  position = forms.CharField(label = 'Posición ')

  def __init__(self,*args,**kwargs):
      super(PlayerForm,self).__init__(*args,**kwargs)
      self.fields['position'].widget.attrs['class'] = 'form-control' 
      self.fields['position'].widget.attrs['placeholder'] = 'Ingrese posición.' 

class PlayerTeamForm(forms.Form):
    team = forms.CharField(label = 'Equipo ')

    def __init__(self,*args,**kwargs):
        super(PlayerTeamForm,self).__init__(*args,**kwargs)
        self.fields['team'].widget.attrs['class'] = 'form-control'
        self.fields['team'].widget.attrs['placeholder'] = 'Ingrese Equipo.'

