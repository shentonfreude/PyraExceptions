============================
 Pyramid Exceptions Testing
============================

We're seeing some strange behavior in a subclass or Pyramid's
HTTPExceptions we're using. So we set up a bare bones Pyramid app to
test our sticky problem and see how we can easily set JSON output for
an API server. We also play with caching.

It's also a chance for me to create a minimal pyramid install, but one
that can use pserve so we can use the `--reload` option.

Install
=======

Set up the virtual env::

  virtualenv --python=python3 .venv3
  source .venv3/bin/activate

We can run pyraexceptions from the command line if we::

  pip install requirements.txt

But to run pserve, we need::

  python setup.py develop

Run it
======

With plain python::

  cd pyraexceptions
  ./__init__.py

With pserve::

  pserve --reload local.ini
