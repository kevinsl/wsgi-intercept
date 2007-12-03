"""work with an intercepted HTTP connection in a webtest.WebCase

webtest_ is an extension to ``unittest`` that has some nice functions for
testing Web sites.

To install the WSGI intercept handler, do ::

    >>> import wsgi_intercept.webtest
    >>> class WSGI_Test(wsgi_intercept.webtest.WebCase):
    ...     HTTP_CONN = wsgi_intercept.WSGI_HTTPConnection
    ...     HOST='localhost'
    ...     PORT=80
    ... 
    ...     def setUp(self):
    ...         wsgi_intercept.add_wsgi_intercept(self.HOST, self.PORT, create_fn)
    ... 
    >>> 

.. _webtest: http://www.cherrypy.org/file/trunk/cherrypy/test/webtest.py

"""

from webtest import *