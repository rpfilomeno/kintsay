from setuptools import setup, find_packages

setup(
    name="kintsay",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "celery[redis]>=5.4.0",
        "smolagents>=1.2.2",
        "litellm>=1.58.2",
    ],
    author="Roger Filomeno",
    author_email="rpfilomeno@gmail.com",
    description="A Celery task wrapper for SmolAgent",
    url="https://github.com/rpfilomeno/kintsay",
    keywords=["celery[redis]", "smolagent", "litellm"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
