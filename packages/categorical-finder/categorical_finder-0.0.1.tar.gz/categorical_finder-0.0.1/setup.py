from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='categorical_finder',
  version='0.0.1',
  description='A Python utility for analyzing and suggesting appropriate encoding methods for categorical columns in CSV datasets.',
  long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
  url='',  
  author='Sri Jaya Karti',
  author_email='srijayakarti@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='categorical', 
  packages=find_packages(),
  install_requires=[''] 
)