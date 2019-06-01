from django.db import models

class ToDoItem(models.Model):
    text = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def mark_done(self):
        self.done = True
        self.save()

    def mark_undone(self):
        self.done = False
        self.save()
