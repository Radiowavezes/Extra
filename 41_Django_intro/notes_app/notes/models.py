from django.db import models

class Notes(models.Model):
    message = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.message}'
