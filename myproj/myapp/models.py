from django.urls import reverse
from django.db import models

class DoTaskList(models.Model):
    name = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    
    def get_absolute_url(self):
        return reverse('myapp:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name