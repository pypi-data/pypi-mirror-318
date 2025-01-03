from setuptools import setup, find_packages

setup(
    name='SelfImplemented-Community-Detection-Algorithms-Improved',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'heapq',
        'collections',
        'matplotlib',
        'numpy',
        'copy',
        'networkx'
    ],
    description='A custom library for community detection algorithms with optimized performance and flexibility',
    author='Emanuele Iaccarino',
    author_email='emanueleiaccarino.ei@gmail.com',
    long_description=open('README.md', encoding='utf-8').read(), 
    long_description_content_type='text/markdown',
    url='https://github.com/emanueleiacca/SelfImplemented-Community-Detection-Algorithms-Improved',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
