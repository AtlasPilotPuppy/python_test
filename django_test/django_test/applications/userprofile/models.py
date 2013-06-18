try:
    import simplejson as json
except:
    import json

from django.db import models
from django.contrib.auth.models import User

class Userprofile(models.Model):

    user = models.ForeignKey(User, related_name='profile')    
    telephone = models.CharField(max_length=15)
    
    
    
class Todo(models.Model):
    user = models.ForeignKey(User, related_name="todo_list")
    list = models.TextField()
    
    def add(self, item, status='active'):
        list = self.get_list()
        list.append({'value':item, 'status':status})
        self.list = json.dumps(list)
        self.save()
    
    def update(self, item):
        list = self.get_list()
        for l in list:
            if l.get('value') == item:
                if l['status'] == "active":
                    l['status'] = "complete"
                else:
                    l['status'] = "active"
                break
                
        self.list = json.dumps(list)
        self.save()
        return l['status']
    
    def remove(self, item):
        list = self.get_list()
        for l in list:
            if l.get('value') == item:
                list.pop(list.index(l))
                break
                
        self.list = json.dumps(list)
        self.save()

    
    def get_list(self):
        if self.list is None or self.list == "":
            todos = []
        else:
            print self.list
            todos = json.loads(self.list)
        return todos

