from setuptools import setup, find_packages

setup(
    name='primetrydemo',              # Package name
    version='0.1.1',               # Initial release version
    description='A simple example package', 
    long_description=open('README.md').read(),  # Long description from README
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/mypackage',  # GitHub repo URL
    packages=find_packages(),      # Automatically find submodules
    package_data={
        '': ['README.md'],  # Explicitly include README.md
    },
    include_package_data=True,
    install_requires=[             # List of dependencies
        'numpy',                   # Example dependency
    ],
    classifiers=[                  # Package metadata
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',       # Python version requirement
)
