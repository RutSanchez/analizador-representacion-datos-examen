from django import forms


class NumeroForm(forms.Form):
    numero = forms.CharField(
        label="Número",
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Ej.: 1010, 255 o FF"})
    )
    base = forms.ChoiceField(
        label="Base de origen",
        choices=[
            ("2", "Binario (base 2)"),
            ("8", "Octal (base 8)"),
            ("10", "Decimal (base 10)"),
            ("16", "Hexadecimal (base 16)"),
        ]
    )


class TextoForm(forms.Form):
    texto = forms.CharField(
        label="Texto (máximo 20 caracteres)",
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Ej.: Año ñ"})
    )
def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["texto"].widget.attrs.pop("maxlength", None)
