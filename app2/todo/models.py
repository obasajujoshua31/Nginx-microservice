from django.db import models

# Create your models here.
class Todo(models.Model):
    item_name = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    user_id = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.item_name
    
    def update_item(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()
        return self
