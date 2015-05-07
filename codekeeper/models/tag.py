from django.db import models


class Tag(models.Model):
    class Meta:
        app_label = 'codekeeper'

    name = models.CharField(max_length=128)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)