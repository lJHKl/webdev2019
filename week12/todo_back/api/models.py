from django.db import models
import datetime
from datetime import timedelta

class TaskList(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id, 
            'name': self.name
        }

class Task(models.Model):
    name = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    due_on = models.DateTimeField()
    status = models.CharField(max_length = 100)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'name': self.name,
            'created_at': self.created_at,
            'due_on': self.due_on,
            'status': self.status
        }
