import os

from setuptools import setup, find_packages

# use pip to parse the requirements.txt files into lists.
#from pip.req import parse_requirements
#reqs = [str(i.req) for i in parse_requirements('requirements.txt',
#                                               session=False)]
#print('Reqs={}'.format(reqs))

# here = os.path.abspath(os.path.dirname(__file__))
# with open(os.path.join(here, 'README.txt')) as f:
#     README = f.read()
# with open(os.path.join(here, 'CHANGES.txt')) as f:
#     CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'waitress',
#    'git+ssh://git@stash.nasawestprime.com:7999/avail/avail.git@develop#egg=avail',
]

setup(name='PyraExceptions',
      version='0.0',
      description='PyraExceptions try exceptions as json',
      # long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="myproject",
      entry_points="""\
      [paste.app_factory]
      main = pyraexceptions:main
      """,
      )
