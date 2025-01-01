from setuptools import setup, find_packages

setup(
    name="lilliepy",
    version="2.0.1",
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
        "reactpy-router",
        "reactpy-forms",
        "reactpy-table",
        "reactpy-select",
        "reactpy-flake8",
        "reactpy-apexcharts",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
