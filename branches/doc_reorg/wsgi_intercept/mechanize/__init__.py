"""intercept connections made using a mechanize Browser.

mechanize_ is John J. Lee's port of Perl's WWW::Mechanize to Python.
It mimics a browser.  (It's also what's behind twill_.)

mechanize is just as easy as mechanoid: ::

   >>> import wsgi_intercept.mechanize
   >>> from wsgi_intercept.test_wsgi_app import create_fn
   >>> wsgi_intercept.add_wsgi_intercept('localhost', 80, create_fn)
   >>> b = wsgi_intercept.mechanize.Browser()

.. _mechanize: http://wwwsearch.sf.net/

"""
from wsgi_browser import Browser