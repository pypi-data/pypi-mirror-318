from setuptools import setup, find_packages

setup(
    name='matrix_operations_zjh',
    version='1.0.0',
    author='zjh',
    author_email='3398727636@qq.com',
    description='A simple package for matrix operations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://www.example.com',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # Add any dependencies here
    ],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    entry_points={
        'console_scripts': [
            'matrix_operations=matrix_operations.operations:main_function',
        ],
    },
)