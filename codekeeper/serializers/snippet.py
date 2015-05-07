from rest_framework import serializers
from codekeeper.models import Person, Snippet, Tag


class PersonSnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'full_name', 'url')


class TagSnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'url')


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    creator = PersonSnippetSerializer()
    tags = TagSnippetSerializer(many=True)

    class Meta:
        model = Snippet
