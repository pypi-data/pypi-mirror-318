from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='zyank',
  version='0.5',
  author='Void Hiko',
  author_email='racomarov@gmail.com',
  description='library for adding basic functions for collecting data from the cian website',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/VoidHiko',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='cyan ,speed searching',
  project_urls={
    'GitHub': 'https://github.com/VoidHiko'
  },
  python_requires='>=3.6'
)