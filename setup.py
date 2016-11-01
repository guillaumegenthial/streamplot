try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
setup(name='streamplot',
      version='0.1',
      description='Real Time Plots with pyqtgraph',
      url="https://github.com/GuillaumeGenthial/streamplot", 
      author='Guillaume Genthial',
      author_email='genthial@stanford.edu',
      license='MIT',
      install_requires=[
          'numpy',
          'pyqtgraph',
      ],
      zip_safe=False)