from setuptools import setup, find_packages

setup(
    name='requetses',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests', 
    ],
    description='A bot for sending images from directories to Telegram',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
