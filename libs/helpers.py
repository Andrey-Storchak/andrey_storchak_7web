import json

from django.http import HttpResponse

def render_to_json_response(context, **response_kwargs):
    '''
    Generates HttpResponse with "application/json" content type in headers
    '''

    response_kwargs['content_type'] = 'application/json'
    return HttpResponse(
        convert_context_to_json(context),
        **response_kwargs)

def convert_context_to_json(context):
    ''' Converts context to json with ugly error handling'''

    try:
        return json.dumps(context)
    except Exception, e:
        return json.dumps({'json_error': e.message})
