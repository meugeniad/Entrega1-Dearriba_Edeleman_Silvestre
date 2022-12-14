from django import forms
from ckeditor.fields import RichTextFormField
 
class BuscarPaisFormulario(forms.Form):
    pais = forms.CharField(max_length=50,required=False)
    
class EditarDestinoFormulario(forms.Form):
    pais = forms.CharField(max_length = 50)
    ciudad = forms.CharField(max_length = 50)
    sugerido_para = forms.CharField(max_length = 100)
    informacion = RichTextFormField()
    autor = forms.CharField(max_length = 50)
    foto_destino = forms.ImageField(label='Foto Destino',required=False)