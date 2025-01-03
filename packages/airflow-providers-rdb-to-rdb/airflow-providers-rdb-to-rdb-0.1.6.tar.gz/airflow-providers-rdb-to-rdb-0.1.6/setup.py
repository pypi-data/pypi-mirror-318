from setuptools import find_packages, setup

setup(
    name="airflow-providers-rdb-to-rdb",
    version="0.1.6",
    author="Aiden Wu",
    author_email="aiden.wu@crypto.com",
    description="A custom Airflow operator to upsert data from PostgreSQL to TiDB.",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Apache Airflow",
        "License :: OSI Approved :: MIT License",
    ],
)
