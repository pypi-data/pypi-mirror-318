from setuptools import setup, find_packages

setup(
    name='your_module',  # Name of your package
    version='0.1',  # Initial version of your package
    packages=find_packages(),  # Automatically find all packages in the module
    include_package_data=True,  # Include files specified in MANIFEST.in
    install_requires=[],  # List any external dependencies here, if applicable
    long_description=open('README.md').read(),  # Read long description from README file
    long_description_content_type='text/markdown',  # Format of the long description
    classifiers=[
        'Programming Language :: Python :: 3',  # Specify that this package is for Python 3
        'License :: OSI Approved :: MIT License',  # Specify the license
        'Operating System :: OS Independent',  # This package is cross-platform
    ],
    python_requires='>=3.6',  # Specify the minimum Python version required
)
