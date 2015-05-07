from rest_framework import views, renderers
from rest_framework.response import Response
from rest_framework.reverse import reverse

from codekeeper.renderers.custom_html_renderer import CustomHTMLRenderer


class HomePageView(views.APIView):
    template_name = 'index.html'
    renderer_classes = (
        CustomHTMLRenderer,
        renderers.JSONRenderer,
        renderers.BrowsableAPIRenderer
    )

    def get(self, request, *args, **kwargs):
        response = Response({
            'tags': reverse('tag-list', request=request),
            'snippets': reverse('snippet-list', request=request),
            'people': reverse('person-list', request=request)
        })
        return response