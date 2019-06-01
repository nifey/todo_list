from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_items, name='list_items'),
    path('done/<int:pk>', views.item_done, name='item_done'),
    path('undo/<int:pk>', views.item_undone, name='item_undone'),
    path('new', views.new_item, name='new_item'),
    path('delete/<int:pk>', views.delete_item, name='delete_item'),
]
