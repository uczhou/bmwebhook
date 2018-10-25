from django.db import models

# Create your models here.
class Message(models.Model):
    from_number = models.CharField(max_length=20)
    to_number = models.CharField(max_length=20)
    text_field = models.CharField(max_lenght= 1000)

    def __str__(self):
        return self.text_field