def serialize(response, query):
    people = []
    snippets = []

    content = {
        'query': query,
        'facets': {
            'facet_fields': response.facet_counts.facet_fields,
        },
        'results': {
            'numFound': len(response),
            'people': people,
            'snippets': snippets
        }
    }

    for item in response:
        item_type = item['type']
        item_id = item['item_id']

        if item_type == 'person':
            rep = {
                'id': item_id,
                'url': '/person/{}'.format(item_id),
                'name': '{} {}'.format(item['first_name'], item['last_name']),
                'last_name': item['last_name'],
                'first_name': item['first_name']
            }
            people.append(rep)

        elif item_type == 'snippet':
            rep = {
                'id': item_id,
                'url': '/snippet/{}'.format(item_id),
                'title': item['title'],
                'snippet': item['snippet'],
                'tags': item['tags']
            }
            snippets.append(rep)

        else:
            # or fail, or log...
            continue

    return content
