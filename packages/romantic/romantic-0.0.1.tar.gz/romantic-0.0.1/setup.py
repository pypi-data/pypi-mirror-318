from setuptools import setup, find_packages

setup(
    name='romantic',
    version='1.0.0',
    description='My personalized love-filled CLI tool ❤️',
    author='Rahul Prajapati',
    author_email='rahul.coder.25@gmail.com',
    packages=find_packages(),  # Automatically finds all packages under the project
    include_package_data=True,  # Includes non-Python files specified in MANIFEST.in
    install_requires=[
        'Click',  # Click is required to handle the CLI functionality
    ],
    entry_points={
        'console_scripts': [
            'baby=romanticCLI.main:baby',  # Maps 'baby' command to baby() function in babyCLI.main module
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Ensure Python version compatibility
)
