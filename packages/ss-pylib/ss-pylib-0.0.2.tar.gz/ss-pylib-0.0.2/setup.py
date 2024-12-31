from setuptools import setup, find_packages

setup(
    name='ss-pylib',
    version='0.0.2',
    description='SWEET-SOOP Python Library',
    author='sweetsoop',
    author_email='sweetsoop@gmail.com',
    license='MIT',
    url='https://github.com/sweetsoop/py-lib.git',
    packages=find_packages(),
    python_requires='>=3.9',
    entry_points={
        'console_scripts': [
            'hey = src.main:main'
        ]
    },
)