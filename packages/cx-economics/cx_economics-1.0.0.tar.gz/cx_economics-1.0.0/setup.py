from setuptools import setup, find_packages

setup(
    name="cx_economics",
    version="1.0.0",
    author="Veera Balakrishnan",
    author_email="mail2veerads@gmail.com",
    description="Analyze CX economics using NPS and revenue data.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    license='MIT',
    packages=find_packages(),
    py_modules=["cx_economics"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
