from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='plapi-string',  # Unique package name on PyPI
    version='0.0.1',  # Package version
    author='plapi',  # Your name
    author_email='plapi.org@gmail.com',  # Your email address
    description='String operations python package',  # Short description
    long_description=long_description,  # Detailed description (from README.md)
    long_description_content_type="text/markdown",  # Long description content type
    url="https://github.com/plapi-org/plapi-string",  # URL to the project repository
    project_urls={  # Additional links
        "Bug Tracker": "https://github.com/plapi-org/plapi-string/issues",
    },
    packages=find_packages(),  # Automatically detect sub-packages
    install_requires=[],  # Required dependencies, e.g., ["numpy>=1.21.0"]
    classifiers=[
        'Development Status :: 4 - Beta',  # Development status: Alpha, Beta, Production/Stable
        'Programming Language :: Python :: 3',  # Supported Python versions
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',  # License
        'Operating System :: OS Independent',  # Supported operating systems
        'Intended Audience :: Developers',  # Target audience
        'Topic :: Software Development :: Libraries :: Python Modules',  # Package topic
    ],
    python_requires='>=3.6',  # Minimum Python version
    keywords="strings nlp operations analysis package",  # Keywords
)
