from setuptools import setup

description='Shorten urls with Google URL shortening service'
setup(name='gush',
      version='1.0.0',
      description=description,
      long_description=description,
      license='MIT',
      author='Luke Lee',
      author_email='durdenmisc@gmail.com',
      url='https://github.com/durden/gush',
      platforms='any',
      classifiers= [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: System :: Archiving'],
      packages=['gush'],
      entry_points={
        "console_scripts": [
            "gush = gush.gush:main",
        ]
      },
)
