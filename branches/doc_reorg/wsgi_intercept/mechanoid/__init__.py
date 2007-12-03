"""intercept connections made using a mechanoid Browser.

mechanoid_ is a fork of mechanize_. ::

   >>> import wsgi_intercept.mechanoid
   >>> from wsgi_intercept.test_wsgi_app import create_fn
   >>> wsgi_intercept.add_wsgi_intercept('some_host', 80, create_fn)
   >>> b = wsgi_intercept.mechanoid.Browser()
   >>> response = b.open('http://some_host:80')
   >>> response.read()
   'WSGI intercept successful!\\n'
   
.. _mechanoid: http://www.python.org/pypi/mechanoid/

"""
from wsgi_browser import Browser