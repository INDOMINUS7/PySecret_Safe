from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='PySecret_Safe',
    version='1.1',
    description='Python secret vault to encrypt and hide your files in a secure place.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ankit Kumar',
    author_email='b21279@students.iitmandi.ac.in',
    url='https://github.com/INDOMINUS7/PySecret_Safe',
    py_modules=['secret_vault'],
    install_requires=['cryptography', 'pyAesCrypt'],
    entry_points={
        'console_scripts': [
            'secret_vault = secret_vault:main',
        ],
    },
    classifiers=[
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
    ],
)
