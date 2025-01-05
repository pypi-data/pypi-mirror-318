from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="deepclimate",
    version="0.1.2",
    author="Midhun Murukesh",
    author_email="midhunmachari@gmail.com",
    description="A deep learning framework for climate modelling and data analysis",
    long_description=long_description, 
    long_description_content_type="text/markdown",
    url="https://github.com/midhunmachari/DeepClimate", 
    packages=find_packages(),
    python_requires=">=3.9", 
    install_requires=[
        "numpy",
        "pandas",
        "scipy",
        "netcdf4",
        "tensorflow==2.17.0",
        "xarray>=2024.11.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
)
