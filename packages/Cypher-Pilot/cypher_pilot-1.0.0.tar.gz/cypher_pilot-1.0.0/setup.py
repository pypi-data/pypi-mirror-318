from setuptools import setup, find_packages

setup(
    name='Cypher-Pilot',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'neo4j>=4.4.0'
    ],
    author='Yaki Naftali',
    author_email='yaki.naftali@accenture.com',
    description='Python Library for Database Interaction with Neo4j',
    long_description_content_type='text/markdown',
    classifiers = [
        'Programming Language :: Python :: 3'
    ] ,
    keywords='Neo4j, Cypher, Database, Python, CSV Export'
)
