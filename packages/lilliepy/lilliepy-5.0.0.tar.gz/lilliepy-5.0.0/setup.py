from setuptools import setup, find_packages

setup(
    name="lilliepy",
    version="5.0.0",
    author="sarthak ghoshal",  
    author_email="sarthak22.ghoshal@example.com",  
    description="A Bundle of Pkgs for Lilliepy",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/websitedeb/lilliepy",  
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "reactpy",
        "reactpy-router"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
