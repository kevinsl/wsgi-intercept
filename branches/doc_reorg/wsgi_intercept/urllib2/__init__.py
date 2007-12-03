
"""intercept http requests made using the urllib2 module.

urllib2_ is a standard Python module, and ``urllib2.urlopen`` is a pretty
normal way to open URLs.

The following code will install the WSGI intercept stuff as a default
urllib2 handler: ::

   >>> from wsgi_intercept.urllib2 import install_opener
   >>> install_opener() #doctest: +ELLIPSIS
   <urllib2.OpenerDirector instance at ...>
   >>> import wsgi_intercept
   >>> from wsgi_intercept.test_wsgi_app import create_fn
   >>> wsgi_intercept.add_wsgi_intercept('some_host', 80, create_fn)
   >>> import urllib2
   >>> urllib2.urlopen('http://some_host:80/').read()
   'WSGI intercept successful!\\n'

The only tricky bit in there is that different handler classes need to
be constructed for Python 2.3 and Python 2.4, because the httplib
interface changed between those versions.

.. _urllib2: http://docs.python.org/lib/module-urllib2.html

"""
from wsgi_urllib2 import install_opener