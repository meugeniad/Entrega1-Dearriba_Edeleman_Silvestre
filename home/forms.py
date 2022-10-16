from django import forms


class DestinoFormulario(forms.Form):
    pais = forms.CharField(max_length = 50)
    ciudad = forms.CharField(max_length = 50)
    informacion = forms.CharField(max_length=500, widget=forms.Textarea)
    sugerido_para = forms.CharField(max_length = 100)
    autor = forms.CharField(max_length = 50)
    
class BuscarPaisFormulario(forms.Form):
    pais = forms.CharField(max_length=50,required=False)