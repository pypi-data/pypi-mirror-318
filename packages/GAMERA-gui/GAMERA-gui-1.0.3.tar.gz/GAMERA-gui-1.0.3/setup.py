from setuptools import setup, find_packages

setup(
    name="GAMERA-gui",  # Replace with your project name
    version="1.0.3",
    author="Devojyoti Kansabanik",
    author_email="dkansabanik@ucar.edu",
    description="GAMERA MHD simulation GUI viewer",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/devojyoti96/GAMERA-gui",  # Replace with your repo URL
    py_modules=["gamera-gui"],              # The script name (without .py)
    entry_points={
        "console_scripts": [
            "gamera-gui = gameragui:main",  # Command-line entry point
        ]
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy",
        "h5py",
        "matplotlib",
        "PyQt5",
        "astropy",
    ],
)
