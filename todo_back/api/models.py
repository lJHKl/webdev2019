from django.db import models
from datetime import datetime,timedelta

# class TaskList(models.Model):
#     name = models.CharField(max_length=250)
#
# class Task(models.Model):
#     name = models.CharField(max_length=250)
#     created_at = models.DateTimeField(default=datetime.now, blank=True)
#     due_on = models.DateTimeField(default=datetime.now, blank=True) + datetime.timedelta(days=1)
#     status = models.CharField(max_length=250)
#     task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

class TaskList(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return '{}: {}'.format(self.id,self.name)

    def to_json(self):
        return {
            'id' : self.id,
            'name': self.name
        }

class Task(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=datetime.now(), blank=True)
    due_on = datetime.now() + timedelta(days=1)
    status = models.CharField(max_length=250)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def str(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'due_on': self.due_on,
            'status': self.status,
        }