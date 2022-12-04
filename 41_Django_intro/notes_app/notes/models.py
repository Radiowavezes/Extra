from django.db import models
from datetime import datetime, date

class Notes(models.Model):
    text = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    reminder = models.BooleanField(True)
    pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)

    def __str__(self):
        return f'''{self.title} 
                   {self.text} 
                   {self.reminder}
                   {self.pub_date.strftime('%d-%m-%Y')}'''

class Category(models.Model):
    headline = models.CharField(max_length=255)
    all_notes = models.ManyToManyField(Notes)
    
    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline
