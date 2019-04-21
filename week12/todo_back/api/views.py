from django.shortcuts import render
from django.http import JsonResponse
from api.models import Task, TaskList

def all_task_lists(request):
    tasklists = TaskList.objects.all()
    json_tasklists = [tl.to_json() for tl in tasklists]
    return JsonResponse(json_tasklists, safe=False)


def one_task_list(request,pk):
    try:
        tasklist_item = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(tasklist_item.to_json())

def one_task_with_id(request, pk):
    try:
        tasklist_item = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(tasklist_item.to_json())


    tasks = tasklists.tasks_set.all()
    json_tasks = [ts.to_json() for ts in tasks]
    return JsonResponse(json_tasks, safe=False)