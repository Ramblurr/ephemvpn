from distutils.core import setup

setup(
    name='ephemvpn',
    version='0.1',
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
        'Fabric==1.6.0',
        'boto==2.6.0',
        'parsedatetime',
    ],
)
