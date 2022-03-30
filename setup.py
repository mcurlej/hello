from setuptools import setup, find_packages

setup(
    name='hello',
    version='0.1.0',
    packages=find_packages(exclude=("tests",)),
    license='MIT',
    author="Martin Čurlej",
    author_email="martin.curlej@gmail.com",
    long_description=open('README.md').read(),
    entry_points={
        "console_scripts": [
            "hello = hello.cli:main",
        ],
    }
)
