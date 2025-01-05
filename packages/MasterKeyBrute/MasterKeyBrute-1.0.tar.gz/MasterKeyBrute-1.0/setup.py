from setuptools import setup

setup(
    name='MasterKeyBrute',
    version='1.0',    
    description='Bruteforce DPAPI encrypted MasterKey File from Windows Credentials Manager',
    url='https://github.com/ProcessusT/MasterKeyBrute',
    author='Processus Thief',
    author_email='processus@thiefin.fr',
    license='GPL-3.0 license',
    packages=['MasterKeyBrute'],
    install_requires=['impacket',
                      'hashlib',
                      'binascii',
                      'argparse',
                      'Cryptodome',
                      'struct',                     
                      ],

    classifiers=[
        'Programming Language :: Python :: 3.11',
    ],
)
