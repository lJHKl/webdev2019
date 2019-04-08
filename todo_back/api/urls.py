from django.urls import path
from . import views
from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'TaskList', views.TaskListViewSet)

urlpatterns = [
    
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('task_lists/', views.tasklist_list),
    path('task_lists/<int:pk>/', views.tasklists_info),
    path('task_lists/<int:pk>/task/', views.tasklist_task)
]



