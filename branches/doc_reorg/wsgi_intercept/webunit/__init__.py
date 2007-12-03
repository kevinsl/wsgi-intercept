
"""work intercepted HTTP connectsion in a webunit test case.

webunit_ is another unittest-like framework that contains nice functions
for Web testing.  (funkload_ uses webunit, too.)

webunit needed to be patched to support different scheme handlers.
The patched package is in webunit/wsgi_webunit/, and the only
file that was changed was webunittest.py; the original is in
webunittest-orig.py.

To install the WSGI intercept handler, do ::

    >>> from httplib import HTTP
    >>> import wsgi_intercept.webunit
    >>> class WSGI_HTTP(HTTP):
    ...     _connection_class = wsgi_intercept.WSGI_HTTPConnection
    ... 
    >>> class WSGI_WebTestCase(wsgi_intercept.webunit.WebTestCase):
    ...     scheme_handlers = dict(http=WSGI_HTTP)
    ... 
    ...     def setUp(self):
    ...         wsgi_intercept.add_wsgi_intercept('127.0.0.1', 80, create_fn)
    ... 
    >>> 

.. _webunit: http://mechanicalcat.net/tech/webunit/
            
"""
from webunittest import WebTestCase
__version__ = '1.3.8'
