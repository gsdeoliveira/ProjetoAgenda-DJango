from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat

def index(request):
    contatos = Contato.objects.order_by('-id').filter(
        mostrar=True
    )
    paginator = Paginator(contatos, 20)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })



def ver_contato(request, contato_id):
    # try:
    #  contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        raise Http404()

    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })
    #  except Contato.DoesNotExist as e:
    #  raise Http404()

def busca(request):
    termo = request.GET.get('termo')

    if termo is None:
        raise Http404
    
    campos = Concat('nome', Value(' '), 'sobrenome')

    """
    contatos = Contato.objects.order_by('-id').filter(
        Q(nome__icontains=termo) | Q(sobrenome__icontains=termo), # Consulta com OR
        mostrar=True
    )
    """

    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )

    paginator = Paginator(contatos, 20)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })