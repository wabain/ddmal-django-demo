from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


def declare_post_save_receiver(sender, type, get_fields):
    @receiver(post_save, sender=sender)
    def solr_index(sender, instance, created, **kwargs):
        from django.conf import settings
        import uuid
        import scorched

        conn = scorched.SolrInterface(settings.SOLR_SERVER)
        records = conn.query(type=type, item_id=instance.id).execute()

        if records:
            conn.delete_by_ids([rec['id'] for rec in records])

        solr_fields = get_fields(instance)
        solr_fields['id'] = str(uuid.uuid4())
        solr_fields['type'] = type

        conn.add(solr_fields)
        conn.commit()

    return solr_index


def declare_post_delete_receiver(sender, type):
    @receiver(post_delete, sender=sender)
    def solr_delete(sender, instance, **kwargs):
        from django.conf import settings
        import scorched

        conn = scorched.SolrInterface(settings.SOLR_SERVER)
        records = conn.query(type=type, item_id=instance.id).execute()

        if records:
            conn.delete_by_ids([rec['id'] for rec in records])
            conn.commit()

    return solr_delete
