from django import forms
from django import forms
from .models import Pedido, Burger

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['name', 'burger', 'amount', 'notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['burger'].queryset = Burger.objects.all()  # Mostrar todas las hamburguesas
        self.fields['burger'].label = "Selecciona una Hamburguesa"
        self.fields['amount'].label = "Cantidad"