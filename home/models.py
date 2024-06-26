from django.db import models

# Create your models here.
class Room(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class message(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)  
    dislikes = models.PositiveIntegerField(default=0)  
    def __str__(self):
        return self.content[0:50]
    