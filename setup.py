try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
setup(name='streamplot',
      version='0.1',
      description='Plots in real time',
      url="https://github.com/GuillaumeGenthial/simpleplot", 
      author='Guillaume Genthial',
      author_email='genthial@stanford.edu',
      license='MIT',
      install_requires=[
          'numpy',
          'pyqtgraph',
      ],
      zip_safe=False)