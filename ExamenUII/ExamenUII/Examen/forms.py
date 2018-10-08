from django import forms
from .models import Palco

class SearchPalco(forms.Form):
    palco = forms.ModelChoiceField(label='Palco',initial='',
                                widget=forms.Select(),
                                 queryset=None)

    def __init__(self,*args,**kwargs):
        super(SearchPalco,self).__init__(*args,**kwargs)
        self.fields['palco'].widget.attrs['class']= 'form-control'
        self.fields['palco'].widget.attrs['placeholder']= 'Ingrese palco.'
        self.fields['palco'].queryset = Palco.objects.values_list('palcoName', flat=True)
class SearchFanDate(forms.Form):
    inicio = forms.CharField()
    final = forms.DateField()

    

    def __init__(self, *args, **kwargs):
        super(SearchFanDate,self).__init__(*args,**kwargs)
        self.fields['inicio'].widget.attrs['class']='form-control'
        self.fields['final'].widget.attrs['class']='form-control'