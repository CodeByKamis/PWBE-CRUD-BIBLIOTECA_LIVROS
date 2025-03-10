from django.shortcuts import render, redirect, get_object_or_404
from .models import Livros
from .forms import ItemForm

def lista_livros(request):
    livros = Livros.objects.all().order_by('-data_criacao')
    if request.method == 'POST':
        pesquisa = request.POST.get('campoPesquisa')
        if pesquisa:
            livros = Livros.objects.filter(titulo__icontains=pesquisa).order_by('-data_criacao')
    return render(request, 'blog/lista_livros.html', {'livros': livros})

def item_creat(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_livros")
    else:
        form = ItemForm()
    return render (request, 'blog/itens_form.html', {'form': form})

def item_update(request, pk):
    item = get_object_or_404(Livros, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item )
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = ItemForm(instance=item)
    return render (request, 'blog/itens_form.html', {'form':form})

def item_delete (request, pk):
    item = get_object_or_404(Livros, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('lista_livros')
    return render(request, 'blog/confirmar_delete.html', {'item': item})
# Create your views here.
