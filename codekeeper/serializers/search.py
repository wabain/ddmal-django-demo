from rest_framework import serializers

from codekeeper.models import Person, Snippet
from codekeeper.serializers.person import PersonSerializer
from codekeeper.serializers.snippet import SnippetSerializer


class SearchSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        print(args, kwargs)
        super().__init__(self, *args, **kwargs)

    def to_representation(self, instance):
        people = []
        snippets = []

        results = {
            'people': people,
            'snippets': snippets
        }

        # Fake the context
        context = {'request': self.context['request']}

        for item in instance:
            item_type = item['type']
            item_id = item['item_id']

            if item_type == 'person':
                rep = PersonSerializer(context=context).to_representation(Person.objects.get(id=item_id))
                people.append(rep)
            elif item_type == 'snippet':
                rep = SnippetSerializer(context=context).to_representation(Snippet.objects.get(id=item_id))
                snippets.append(rep)

            else:
                # or fail, or log...
                continue

        results['numFound'] = sum(len(v) for v in results.values())

        return {'results': results}
