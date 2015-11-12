#!/usr/bin/env python3
import json
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPOk

from avail.rest.jsonexceptions import JSONOk


@view_config(route_name='root', renderer='json')
def root(request):
    return {'msg': 'Try /ok, /notstickyhtml, /notstickyjson, /exception, /headers, /cache'}

@view_config(route_name='ok', renderer='json', request_method='GET')
def ok(request):
    """We don't need HTTPOk when... we're OK."""
    return {'msg': 'This looks like a method={}'.format(request.method)}

@view_config(route_name='notstickyhtml', renderer='json', request_method='GET')
def notstickyhtml(request):
    """Our app exceptions set sticky singleton, but Pyramid doesn't."""
    _unused = HTTPOk('am I sticky?')
    _unused = HTTPOk(body='is my body sticky?')
    return HTTPOk()             # HTML; does NOT emit the above msgs!

@view_config(route_name='notstickyjson', renderer='json', request_method='GET')
def notstickyjson(request):
    """Our app exceptions set sticky singleton, but Pyramid doesn't."""
    _unused = HTTPOk(json.dumps({'default': 'am I sticky?'}),
                     content_type='application/json')
    _unused = HTTPOk(body=json.dumps({'body': 'is it sticky?'}),
                     content_type='application/json')
    return HTTPOk(body=json.dumps({'msg': 'No stickiness here'}),
                  content_type='application/json')

@view_config(route_name='exception', renderer='json', request_method='GET')
def exception(request):
    """Must set content type and body for JSON exception."""
    return HTTPOk(body=json.dumps({'err': 'bad name'}),
                  content_type='application/json') # OK!
    # None of the following work:
    # return HTTPOk('bad name') # text/html
    # return HTTPOk({'err': 'bad name'}) # text/html unicode escaped
    # raise HTTPOk({'err': 'bad name'}) # text/html unicode escaped
    # return HTTPOk(json.dumps({'err': 'bad name'}),
    #                     content_type='application/json') # text/html unicode escaped
    # return HTTPOk(body={'err': 'bad name'},
    #                     content_type='application/json') # application/json but no body out

@view_config(route_name='headers', renderer='json', request_method='GET')
def headers(request):
    """We can add headers to JSON exception."""
    return HTTPOk(body=json.dumps({'msg': 'got headers?'}),
                  content_type='application/json')

@view_config(route_name='cache', renderer='json', request_method='GET', http_cache=42)
def cache(request):
    """We can set caching in the view_config."""
    return HTTPOk(body=json.dumps({'msg': 'check headers Cache-Control, Expires'}),
                  content_type='application/json')

@view_config(route_name='jsonokstr', renderer='json', request_method='GET')
def jsonokstr(request):
    return JSONOk("a string message, not payload=")

@view_config(route_name='jsonokstr2', renderer='json', request_method='GET')
def jsonokstr2(request):
    JSONOk("I am not the return value! I am a bug.")
    return JSONOk()             # BUG! returns the string above!

@view_config(route_name='jsonokpayload', renderer='json', request_method='GET')
def jsonokpayload(request):
    JSONOk(payload={'msg': 'I am not the return value! I am a bug.'})
    return JSONOk()             # Good: returns {}


def main(global_config, **settings):
    """For pserve, offers --reload"""
    config = Configurator()
    config.add_route('root', '')
    config.add_route('ok', '/ok')
    config.add_route('notstickyhtml', '/notstickyhtml')
    config.add_route('notstickyjson', '/notstickyjson')
    config.add_route('exception', '/exception')
    config.add_route('headers', '/headers')
    config.add_route('cache', '/cache')
    config.add_route('jsonokstr', '/jsonokstr')
    config.add_route('jsonokstr2', '/jsonokstr2')
    config.add_route('jsonokpayload', '/jsonokpayload')
    config.scan()
    return config.make_wsgi_app()

if __name__ == '__main__':
    """For invoking directly with python (no reload)"""
    app = main(global_config={})
    server = make_server('127.0.0.1', 6543, app)
    server.serve_forever()
