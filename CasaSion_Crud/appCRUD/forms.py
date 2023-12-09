from django import forms
from appCRUD.models import *
from django.core.validators import MaxLengthValidator,MinLengthValidator

class BootstrapTextarea(forms.Textarea):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs['class'] = 'form-control'  # Agregamos la clase de Bootstrap
        self.attrs['style'] = 'height: 50px;'


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = UsuarioCRUD
        fields = ['nombre', 'apellido', 'rut', 'email', 'direccion', 'comuna', 'fecha','numero','codCA']

    nombre = forms.CharField(
        label="Ingrese su nombre",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        validators=[
            MaxLengthValidator(limit_value=30)
        ]
    )
    apellido = forms.CharField(
        label="Ingrese su apellido",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        validators=[
            MaxLengthValidator(limit_value=30)
        ]
    )
    rut = forms.CharField(
        label="Ingrese su rut",
        max_length=10,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        validators=[
            MinLengthValidator(limit_value=9),
            MaxLengthValidator(limit_value=10),
        ]
    )
    email = forms.EmailField(
        label="Ingrese su email",
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    direccion = forms.CharField(
        label="Ingrese la direccion",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        validators=[
            MaxLengthValidator(limit_value=30)
        ]
    )
    comuna = forms.CharField(
        label="Ingrese su comuna",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        validators=[
            MaxLengthValidator(limit_value=30)
        ]
    )
    fecha = forms.DateField(
        label="Fecha de nacimiento en el formato de Año-Mes-Dia",
        widget=forms.DateInput(attrs={"class": "form-control"})
    )
    class TuFormulario(forms.Form):
        numero = forms.IntegerField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    codCA = forms.ModelChoiceField(
        queryset=casasAvivamiento.objects.all(), 
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Casa de Avivamiento',
        empty_label=('Elige una Casa de Avivamiento')
    )

class FormFiltroLista(forms.Form):
    codCA = forms.ModelChoiceField(
        queryset=casasAvivamiento.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Filtro por Casa de Avivamiento',
        empty_label='Elige una Casa de Avivamiento',
        required=False,
    )

    nombre = forms.CharField(
    label='Filtro por Nombre',
    widget=BootstrapTextarea(attrs={'placeholder': 'Filtro por Nombre', 'id': 'floatingTextarea'}),
    required=False
    )
