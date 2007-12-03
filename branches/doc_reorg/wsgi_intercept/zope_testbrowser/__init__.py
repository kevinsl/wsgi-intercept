"""intercepting HTTP connections made using zope.testbrowser.

zope.testbrowser_ is a prettified interface to mechanize_ that is used
primarily for testing Zope applications.

zope.testbrowser is also pretty easy ::
    
    >>> import wsgi_intercept.zope_testbrowser
    >>> from wsgi_intercept.test_wsgi_app import create_fn
    >>> wsgi_intercept.add_wsgi_intercept('localhost', 80, create_fn)
    >>> b = wsgi_intercept.zope_testbrowser.WSGI_Browser()
            
.. _zope.testbrowser: http://www.python.org/pypi/zope.testbrowser

"""
from wsgi_testbrowser import WSGI_Browser