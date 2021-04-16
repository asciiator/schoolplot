from setuptools import setup

setup(name='schoolplot',
      version='0.1',
      description='Make axis with arrowtips and through the center',
      author='Johannes Wickles',
      author_email='johannes.wickles@mail.de',
      packages=['schoolplot'],
        install_requires=[
          'matplotlib',
      ],
      zip_safe=False)
