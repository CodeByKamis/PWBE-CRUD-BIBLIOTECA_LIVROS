from django.shortcuts import render, redirect, get_object_or_404
from .models import Livros
from .forms import ItemForm
# Esse def serve para os livros cadastrados aparecerem na home em ordem de criação
def lista_livros(request):
    livros = Livros.objects.all().order_by('-data_criacao')
    # esse if serve para filtragem de livros buscados no campo de pesquisa pelo usuário
    if request.method == 'POST':
        pesquisa = request.POST.get('campoPesquisa')
        if pesquisa:
            livros = Livros.objects.filter(titulo__icontains=pesquisa).order_by('-data_criacao')
            #titulo__icontains serve para que todos os livros que contenham aquelas informações que o usuário buscou apareça, se ele pesquisar '1' todos que tem 1 aparece
    return render(request, 'blog/lista_livros.html', {'livros': livros})

# def responsável pelo botao de criar um novo post
def item_creat(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_livros")
    else:
        form = ItemForm()
    return render (request, 'blog/itens_form.html', {'form': form})

# def responsável pelo botao de editar, onde o usuário pode alterar o post que quiser
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

# def responsável pelo botao de deletar qualquer post que o usuário fez
def item_delete (request, pk):
    item = get_object_or_404(Livros, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('lista_livros')
    return render(request, 'blog/confirmar_delete.html', {'item': item})
# Create your views here.
