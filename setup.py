from setuptools import setup, find_packages


setup(
    name='sedastrela-is',
    version='0.0.0',
    description='IS for scout group Seda Strela',
    url='https://github.com/ondrejsika/sedastrela-is',
    author='Ondrej Sika',
    author_email='ondrej@ondrejsika.com',
    packages=find_packages(),
    install_requires=[
        'django==1.8.8',
        'requests==2.9.1',
        'gunicorn==19.4.5',
     ],
)

