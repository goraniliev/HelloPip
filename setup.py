from distutils.core import setup
setup(
  name = 'hello_pip',
  packages = ['hello_pip'], # this must be the same as the name above
  version = '0.1',
  description = 'A random test lib',
  author = 'Goran Iliev',
  author_email = 'goraniliev93@gmail.com',
  url = 'https://github.com/goraniliev/HelloPip', # use the URL to the github repo
  download_url = 'https://github.com/goraniliev/HelloPip/tarball/0.1', # I'll explain this in a second
  keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers = [],
)