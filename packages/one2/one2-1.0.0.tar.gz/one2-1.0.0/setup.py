from setuptools import setup, find_packages

setup(
    name="one2",  
    version="1.0.0",  
    author="Hadi Raza",
    author_email="hadiraza.9002@gmail.com",
    description="A module to print sequences from 1 to large ranges",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/unknownmeovo/one2",  
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    license="Apache License 2.0",  
    python_requires='>=3.6',
)
