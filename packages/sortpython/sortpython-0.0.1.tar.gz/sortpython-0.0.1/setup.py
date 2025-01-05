from setuptools import setup, find_packages

setup(
    name="sortpython",  # Unique name for your package
    version="0.0.1",  # Initial version
    author="Rukmal Senavirathne",
    description="A Python package for various sorting algorithms",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rukmals/sortpy",  # Replace with your GitHub repo
    packages=find_packages(),  # Automatically finds packages in your directory
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['matplotlib'],
    python_requires=">=3.6",  # Specify compatible Python versions
)
