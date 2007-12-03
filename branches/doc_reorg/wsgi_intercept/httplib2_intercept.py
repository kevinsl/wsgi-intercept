
"""intercept HTTP connections that use httplib2

httplib2_ is a 3rd party extension of the built-in ``httplib``.  To intercept 
requests, it is similar to urllib2::

    >>> from wsgi_intercept.httplib2_intercept import install
    >>> install()
    >>> import wsgi_intercept
    >>> from wsgi_intercept.test_wsgi_app import create_fn
    >>> wsgi_intercept.add_wsgi_intercept('some_host', 80, create_fn)
    >>> import httplib2
    >>> resp, content = httplib2.Http().request('http://some_host:80/', 'GET') 
    >>> content
    'WSGI intercept successful!\\n'

(Contributed by `David "Whit" Morris`_.)

.. _httplib2: http://code.google.com/p/httplib2/
.. _David "Whit" Morris: http://public.xdi.org/=whit

"""

import httplib2
import wsgi_intercept
from httplib2 import HTTPConnectionWithTimeout, HTTPSConnectionWithTimeout
import sys

InterceptorMixin = wsgi_intercept.WSGI_HTTPConnection

# might make more sense as a decorator

def connect(self):
    """
    Override the connect() function to intercept calls to certain
    host/ports.
    """
    if wsgi_intercept.debuglevel:
        sys.stderr.write('connect: %s, %s\n' % (self.host, self.port,))

    try:
        (app, script_name) = self.get_app(self.host, self.port)
        if app:
            if wsgi_intercept.debuglevel:
                sys.stderr.write('INTERCEPTING call to %s:%s\n' % \
                                 (self.host, self.port,))
            self.sock = wsgi_intercept.wsgi_fake_socket(app,
                                                        self.host, self.port,
                                                        script_name)
        else:
            self._connect()

    except Exception, e:
        if wsgi_intercept.debuglevel:              # intercept & print out tracebacks
            traceback.print_exc()
        raise

class HTTP_WSGIInterceptorWithTimeout(HTTPConnectionWithTimeout, InterceptorMixin):
    _connect = httplib2.HTTPConnectionWithTimeout.connect
    connect = connect

class HTTPS_WSGIInterceptorWithTimeout(HTTPSConnectionWithTimeout, InterceptorMixin):
    _connect = httplib2.HTTPSConnectionWithTimeout.connect
    connect = connect

def install():
    httplib2.HTTPConnectionWithTimeout = HTTP_WSGIInterceptorWithTimeout
    httplib2.HTTPSConnectionWithTimeout = HTTPS_WSGIInterceptorWithTimeout

def uninstall():
    httplib2.HTTPConnectionWithTimeout = HTTPConnectionWithTimeout
    httplib2.HTTPSConnectionWithTimeout = HTTPSConnectionWithTimeout
