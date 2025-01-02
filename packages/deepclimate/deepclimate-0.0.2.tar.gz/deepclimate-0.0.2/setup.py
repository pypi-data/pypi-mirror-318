from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="deepclimate",
    version="0.0.2",
    author="Midhun Murukesh",
    author_email="midhunmachari@gmail.com",
    description="A deep learning framework for climate modelling and data analysis",
    long_description=long_description, 
    long_description_content_type="text/markdown",
    # url="https://github.com/midhunmachari/DeepClimate", 
    packages=find_packages(),
    python_requires=">=3.12",
    install_requires=[
        "keras>=3.7.0",
        "matplotlib>=3.10.0",
        "matplotlib-inline>=0.1.7",
        "netcdf4>=1.7.2",
        "numpy>=1.26.4",
        "pandas>=2.2.3",
        "scikit-learn>=1.5.2",
        "scipy>=1.14.1",
        "tabulate>=0.9.0",
        "tensorboard==2.17.1",
        "tensorboard-data-server==0.7.2",
        "tensorflow==2.17.0",
        "tqdm>=4.67.1",
        "xarray>=2024.11.0",
    ],
    classifiers=[
        # Pick those that apply to your project (see PyPI classifiers list)
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
