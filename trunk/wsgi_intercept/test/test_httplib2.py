#! /usr/bin/env python2.4
from wsgi_intercept import httplib2_intercept
from nose.tools import with_setup, raises
from socket import gaierror
import wsgi_intercept
from wsgi_intercept import test_wsgi_app
import httplib2

_saved_debuglevel = None


def install():
    _saved_debuglevel, wsgi_intercept.debuglevel = wsgi_intercept.debuglevel, 1
    httplib2_intercept.install()
    wsgi_intercept.add_wsgi_intercept('some_hopefully_nonexistant_domain', 80, test_wsgi_app.create_fn)

def uninstall():
    wsgi_intercept.debuglevel = _saved_debuglevel
    httplib2_intercept.uninstall()

@with_setup(install, uninstall)
def test_success():
    http = httplib2.Http()
    resp, content = http.request('http://some_hopefully_nonexistant_domain:80/', 'GET')
    assert test_wsgi_app.success()

@with_setup(install, uninstall)
@raises(gaierror)
def test_bogus_domain():
    wsgi_intercept.debuglevel = 1;
    httplib2_intercept.HTTP_WSGIInterceptorWithTimeout("_nonexistant_domain_").connect()
