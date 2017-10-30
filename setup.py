from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='roslaunch_api_wrapper',
      version='0.6',
      description='wrapper for rosalunch python api',
      long_description=readme(),
      url='https://github.com/ACarfi/roslaunch_api_wrapper',
      author='Alessandro Carfi',
      author_email='carfi.alessandro@gmail.com',
      license='MIT',
      packages=['roslaunch_api_wrapper'],
      zip_safe=False)
