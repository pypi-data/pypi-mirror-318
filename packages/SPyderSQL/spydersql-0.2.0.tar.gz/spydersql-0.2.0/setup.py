from setuptools import setup, find_packages


setup(
    name="SPyderSQL",
    version="0.2.0",
    author="Emil Artemev",
    author_email="jordanman1300@gmail.com",
    description='SPyderSQL is a modern ORM framework for SQL database in Python.',
    long_description=open("README.rst", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url='https://github.com/RealWakeArmilus/SPyderSQL',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests>=2.32.0",
        "numpy>=1.19.0",
        "pytest>=6.2.5",
        "flake8>=3.9.2",
        "setuptools~=75.6.0",
        "aiosqlite~=0.20.0"
    ],
    python_requires=">=3.6",
)
