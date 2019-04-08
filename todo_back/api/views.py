from django.http import JsonResponse
from .models import TaskList
from .models import Task
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import TaskListSerializer


class TaskListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer




def tasklist_list(request):
    tasklists = TaskList.objects.all()
    json_tasklists = [tl.to_json() for tl in tasklists]
    return JsonResponse(json_tasklists, safe=False)


def tasklists_info(request,pk):
    try:
        tasklist_item = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(tasklist_item.to_json())

def tasklist_task(request, pk):
    try:
        tasklist_item = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(tasklist_item.to_json())


    tasks = tasklists.tasks_set.all()
    json_tasks = [ts.to_json() for ts in tasks]
    return JsonResponse(json_tasks, safe=False)




