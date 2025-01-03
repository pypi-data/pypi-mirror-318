from setuptools import setup, find_packages

setup(
    name="refkeeper",
    version="0.0.1",
    author="Michael",
    author_email="michaelhanley11@gmail.com",
    description="A tool for managing and validating research references",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/michaeljhanley",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6",
)