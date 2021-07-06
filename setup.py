from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='randcircuit',
      version='0.01',
      description='A simple random circuit generator',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/sspickle/randcircuit',
      author='Steve Spicklemire',
      author_email='steve@spvi.com',
      license='MIT',
      packages=['randcircuit'],
      zip_safe=False,
)
