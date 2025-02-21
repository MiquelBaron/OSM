from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from datetime import datetime, timedelta
from django.db.models import Sum, Count
# Create your views here.


def nuevo(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nuevo')
        else:
            print('El formulario no es valido')
    else:
        form = PedidoForm()
    burgers = Burger.objects.all()
    return render(request, 'nuevo.html', {'form': form, 'burgers': burgers})


def lista(request):
    pedidos = Pedido.objects.all()
    return render(request, 'lista.html', {'pedidos': pedidos})

def marcar(request, id):
    pedido = get_object_or_404(Pedido, pk=id)
    pedido.status = 'D'
    pedido.save()
    return redirect('lista')


def eliminar(request, id):
    pedido = get_object_or_404(Pedido, pk=id)
    pedido.delete()
    return redirect('lista')

def modificar(request, id):
    pedido = get_object_or_404(Pedido, pk=id)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('lista')
        else:
            print('El formulario no es valido')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'modificar.html', {'form': form})

def cocina(request):
    pedidos = Pedido.objects.all()
    return render(request, 'cocina.html', {'pedidos': pedidos})

def progreso(request, id):
    pedido = get_object_or_404(Pedido, pk=id)
    pedido.status = 'I'
    pedido.save()
    return redirect('cocina')

def listo(request,id):
    pedido = get_object_or_404(Pedido, pk=id)
    pedido.status = 'R'
    pedido.save()
    return redirect('cocina')

from django.shortcuts import render
from django.db.models import Sum, Count
from .models import Pedido, Burger
from datetime import datetime, timedelta

def entregado(request):
    # Obtener pedidos entregados
    pedidos = Pedido.objects.filter(status='D')

    # Obtener la fecha actual
    hoy = datetime.now().date()

    # Calcular total recaudado del día
    total_dia = pedidos.filter(date__date=hoy).aggregate(total=Sum('burger__price'))['total'] or 0

    # Calcular total recaudado del mes
    inicio_mes = hoy.replace(day=1)
    total_mes = pedidos.filter(date__gte=inicio_mes).aggregate(total=Sum('burger__price'))['total'] or 0

    # Calcular total histórico recaudado
    total_historico = pedidos.aggregate(total=Sum('burger__price'))['total'] or 0

    # Obtener la hamburguesa más pedida
    hamburguesa_mas_pedida = (
        Burger.objects.annotate(total_pedidos=Count('pedido'))
        .order_by('-total_pedidos')
        .first()
    )

    # Otras características relevantes (ejemplo: pedido más grande)
    pedido_mas_grande = pedidos.order_by('-amount').first()

    return render(request, 'entregados.html', {
        'pedidos': pedidos,
        'total_dia': total_dia,
        'total_mes': total_mes,
        'total_historico': total_historico,
        'hamburguesa_mas_pedida': hamburguesa_mas_pedida,
        'pedido_mas_grande': pedido_mas_grande,
    })






















