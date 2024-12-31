from setuptools import setup, find_packages

setup(
    name="sachin-super-test",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0"
    ],
    author="Sachin Kant",
    author_email="sachin-ext@superleap.com",
    description="A Python SDK for the Superleap API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/superleapai/superleap-sdk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)