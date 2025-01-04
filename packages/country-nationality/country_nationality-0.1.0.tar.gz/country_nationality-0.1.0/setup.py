# setup.py

from setuptools import setup, find_packages

setup(
    name="country_nationality",                  # Package name
    version="0.1.0",                            # Initial version
    packages=find_packages(),                   # Automatically find all packages in the directory
    install_requires=[],                        # List any dependencies here (empty for now)
    author="Anand MC",                         # Your name
    author_email="anand.mc.ofcl@gmail.com",      # Your email address
    description="A Python package to get nationality by country code",
    long_description=open('README.md').read(),  # Load the README content for long description
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # You can change the license if you wish
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version required
)
