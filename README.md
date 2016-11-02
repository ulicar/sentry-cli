# sentry-cli
Pure python CLI for Sentry service

Build rpm:
  python setup.py bdist_rpm
  
Usage without installation:
    touch sentry-cli/sentry/__init__.py
    ./sentry-cli -h


from sentry.client import Client

sentry = Client('token', 'sentry.com')
print (sentry.get_organanizations())

