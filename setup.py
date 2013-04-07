from distutils.core import setup

from ephemvpn import __version__

setup(
    name='ephemvpn',
    version=__version__,
    author='Casey Link',
    author_email='unnamedrambler@gmail.com',
    packages=['ephemvpn'],
    scripts=['bin/ephemvpn'],
    url='https://github.com/Ramblurr/ephemvpn',
    license='BSD-3',
    description='Launch ephemeral VPNs on EC2',
    long_description=open('README.md').read(),
    package_data={'ephemvpn': ['*.txt', 'vpntypes/data/*']},
    install_requires=[
        'Fabric==1.4.3',
        'boto==2.6.0',
        'parsedatetime',
    ],
)
