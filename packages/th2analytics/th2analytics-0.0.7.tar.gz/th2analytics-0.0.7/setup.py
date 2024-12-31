from setuptools import setup, find_packages

setup(
    name="th2analytics",
    version="0.0.7",
    description="A Python package for interacting with the thaink2 analytics APIs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Farid Azouaou",
    author_email="contact@thaink2.com",
    url="https://github.com/thaink2/th2analytics_py", 
    packages=find_packages(),
    install_requires=["requests","json","argparse"], 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)