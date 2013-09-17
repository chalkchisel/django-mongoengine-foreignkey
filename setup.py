#!/usr/bin/env python
import mongofk

from distutils.core import setup


description = "An implementation of a foreign key field for mongoengine " \
    "that references a Django model object."

setup(
    name='django-mongoengine-foreignkey',
    version=mongofk.__version__,
    author='Joshua Ourisman',
    author_email='josh@bolsterlabs.com',
    url='https://github.com/bolster/django-mongoengine-foreignkey',
    description=description,
    long_description=description,
    license='BSD',
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    packages=['mongofk', ],
)
