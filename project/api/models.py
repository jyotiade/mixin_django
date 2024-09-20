from django.db import models

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(max_length=50)
    style = models.CharField(max_length=50)

    class Meta:
        ordering = ['created']