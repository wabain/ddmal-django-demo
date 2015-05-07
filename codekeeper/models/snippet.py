from django.db import models

from codekeeper.helpers import solrsync


class Snippet(models.Model):
    class Meta:
        app_label = 'codekeeper'

    title = models.CharField(max_length=256, blank=True, null=True)
    snippet = models.TextField()

    tags = models.ManyToManyField('codekeeper.Tag')
    creator = models.ForeignKey('codekeeper.Person')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)


solr_index = solrsync.declare_post_save_receiver(Snippet, 'snippet', lambda i: {
    'item_id': i.id,
    'snippet': i.snippet,
    'title': i.title,
    'tags': [t.name for t in i.tags.all()]
})

solr_delete = solrsync.declare_post_delete_receiver(Snippet, 'snippet')
