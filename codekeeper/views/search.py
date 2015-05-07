from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
# from rest_framework import status
from rest_framework.renderers import JSONRenderer

from django.conf import settings
import scorched

# from codekeeper.serializers.search import SearchSerializer
from codekeeper.helpers import format_solr
from codekeeper.renderers.custom_html_renderer import CustomHTMLRenderer


class SearchViewHTMLRenderer(CustomHTMLRenderer):
    template_name = "search/search.html"


class SearchView(GenericAPIView):
    # serializer_class = SearchSerializer
    renderer_classes = (JSONRenderer, SearchViewHTMLRenderer)

    def get(self, request, *args, **kwargs):
        fields = ['tags', 'first_name', 'last_name', 'title']

        query = request.GET

        solr_query = {'text': query.get('q')}

        solr_query.update((field, query[field]) for field in fields if field in query)

        if not query:
            return Response({'results': None})

        conn = scorched.SolrInterface(settings.SOLR_SERVER)
        resp = conn.query(**solr_query).facet_by(fields).execute()

        return Response(format_solr.serialize(resp, query.get('q')))