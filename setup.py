from setuptools import setup

setup(name='tropopause',
      version='0.2',
      description='Extra utilities for troposphere',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
      ],
      url='http://github.com/adragomir/tropopause',
      author='Andrei Dragomir',
      author_email='adragomir@gmail.com',
      license='MIT',
      packages=['tropopause'],
      install_requires=[
          'troposphere',
          'awacs'
      ],
      zip_safe=True)
