from rest_framework import serializers
from codekeeper.models import Person, Snippet


class SnippetPersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ('url', 'title')
        model = Snippet


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    snippets = SnippetPersonSerializer(source='snippet_set', many=True)

    class Meta:
        fields = ('first_name', 'last_name', 'full_name', 'snippets')
        model = Person