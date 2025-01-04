from setuptools import setup, find_packages

setup(
    name='zscryptography',
    version='2.0.0',
    packages=find_packages(),
    install_requires=[
        'cryptography',
    ],
    author='ZSU',
    author_email='',
    description='A simple cryptography library using AES',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/zsu/zscryptography',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)