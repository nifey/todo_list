from django.shortcuts import render, get_object_or_404, redirect

from .models import ToDoItem
from .forms import ToDoItemForm

def list_items(request):
    list = ToDoItem.objects.all()
    form = ToDoItemForm()
    return render(request, 'todo/list_items.html', {'list' : list, 'form' : form})

def item_done(request, pk):
    item = get_object_or_404(ToDoItem, pk=pk)
    item.mark_done()
    return redirect('list_items')

def item_undone(request, pk):
    item = get_object_or_404(ToDoItem, pk=pk)
    item.mark_undone()
    return redirect('list_items')

def new_item(request):
    if request.method == 'POST':
        form = ToDoItemForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('list_items')

def delete_item(request, pk):
    item = get_object_or_404(ToDoItem, pk=pk)
    item.delete()
    return redirect('list_items')
