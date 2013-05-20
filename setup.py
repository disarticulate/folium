# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='folium',
    version='0.1.0',
    description='Make beautiful maps with Leaflet.js & Python',
    author='Rob Story',
    author_email='wrobstory@gmail.com',
    license='MIT License',
    url='https://github.com/wrobstory/folium',
    keywords='data visualization',
    classifiers=['Development Status :: 3 - Alpha',
                 'Programming Language :: Python :: 2.7',
                 'License :: OSI Approved :: MIT License'],
    packages=['folium'],
    package_data={'': ['*.js',
                       '*.css',
                       'templates/*.html',
                       'templates/*.js',
                       'templates/*.txt',
                       'plugins/*.css',
                       'plugins/*.js']}
)
