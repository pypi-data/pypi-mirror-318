from setuptools import setup, find_packages

setup(
    name='simpleCan',
    version='0.2',
    packages=find_packages(),
    author='JIAJIE LIU',
    author_email='ljj26god@163.com',
    description='This package realizes sending can message functionality',
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)