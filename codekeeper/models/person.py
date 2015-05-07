from django.db import models

from codekeeper.helpers import solrsync


class Person(models.Model):
    class Meta:
        app_label = 'codekeeper'
        verbose_name_plural = 'people'

    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return '{}, {}'.format(self.last_name, self.first_name)


solr_index = solrsync.declare_post_save_receiver(Person, 'person', lambda i: {'item_id': i.id,
                                                                              'first_name': i.first_name,
                                                                              'last_name': i.last_name})

solr_delete = solrsync.declare_post_delete_receiver(Person, 'person')
