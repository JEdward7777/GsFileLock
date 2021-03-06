from distutils.core import setup

setup(
    name='GsFileLock',
    version='0.1.0',
    author='Evan Fosmark',
    author_email='me@evanfosmark.com',
    packages=['gsfilelock','gsfilelock.test'],
    url='https://github.com/JEdward7777/GsFileLock',
    license='LICENSE.txt',
    description='Google Storage File locking library',
    long_description=open('README.txt').read(),
)
