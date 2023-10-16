from django.db import models
from django.urls import reverse

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    named_url = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Древовидное меню'
        verbose_name_plural = 'Древовидное меню'
        ordering = ['name']
