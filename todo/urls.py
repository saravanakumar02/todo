from django.urls import path
from . import views

urlpatterns = [
    # add task
    path('addTask/', views.addTask, name='addTask'),

    # mark as done
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    
    # undo
    path('undo/<int:pk>/', views.undo, name='undo'),

    # edit
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),

    # delete
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),

]