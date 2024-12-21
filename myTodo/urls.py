from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('todo/', views.todo_list, name="todo_list"),
    path('todo/create/', views.create_todo, name="create_todo"),
    path('todo/<int:todo_id>/complete/', views.complete_todo, name='complete_todo'),
    path('todo/<int:todo_id>/delete/', views.delete_todo, name='delete_todo'),
    path('admin/', admin.site.urls),
]
