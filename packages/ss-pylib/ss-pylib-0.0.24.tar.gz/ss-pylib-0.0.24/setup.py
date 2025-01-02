from setuptools import find_packages, setup


with open('README.md', encoding='utf-8') as fd:
  long_description = fd.read()

setup(
  name='ss-pylib',
  version='0.0.24',
  description='SWEET-SOOP Python Library',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author='sweetsoop',
  author_email='sweetsoop@gmail.com',
  license='MIT',
  packages=find_packages(),
  python_requires='>=3.11',
  entry_points={
    'console_scripts': [
      'hey = sslib.main:main'
    ]
  },
  install_requires=[
    'httpx', 'PyMySQL',
  ],
)