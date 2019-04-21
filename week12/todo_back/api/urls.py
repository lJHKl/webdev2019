from django.urls import path
from api import views

urlpatterns = [
    path('task_lists/', views.all_task_lists),
    path('task_lists/<int:pk>/', views.one_task_list),
    path('task_lists/<int:pk>/task/', views.one_task_with_id)
]