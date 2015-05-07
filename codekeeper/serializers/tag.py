from rest_framework import serializers
from codekeeper.models import Tag, Snippet, Person


class PersonSnippetTagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'full_name', 'url')


class SnippetTagSerializer(serializers.HyperlinkedModelSerializer):
    creator = PersonSnippetTagSerializer()

    class Meta:
        fields = ('title', 'creator', 'url')
        model = Snippet


class TagSerializer(serializers.HyperlinkedModelSerializer):
    snippets = SnippetTagSerializer(source='snippet_set', many=True)

    class Meta:
        model = Tag