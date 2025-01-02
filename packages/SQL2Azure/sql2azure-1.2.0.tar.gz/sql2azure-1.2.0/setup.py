from setuptools import setup, find_packages

setup(
    name='SQL2Azure',
    version='1.2.0',
    description='Load data from an on-prem SQL database to Azure Storage as JSON or CSV.',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url='https://github.com/mr-speedster/SQL2Azure',
    author='Ajith D',
    author_email='ajithd78564@gmail.com',
    license="MIT",
    packages=find_packages(),
    install_requires=[
        'pyodbc',
        'azure-storage-blob',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)