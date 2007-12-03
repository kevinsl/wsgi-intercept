"""intercept connections made using a mechanoid Browser.

mechanoid_ is a fork of mechanize_.

mechanoid is pretty easy; just use ::

   >>> import wsgi_intercept.mechanoid
   >>> from wsgi_intercept.test_wsgi_app import create_fn
   >>> wsgi_intercept.add_wsgi_intercept('localhost', 80, create_fn)
   >>> b = wsgi_intercept.mechanoid.Browser()
   
.. _mechanoid: http://www.python.org/pypi/mechanoid/

"""
from wsgi_browser import Browser