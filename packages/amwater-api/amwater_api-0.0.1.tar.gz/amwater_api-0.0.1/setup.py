import setuptools

with open("README.md", "r") as fh:
    long_description=fh.read()

setuptools.setup(
    name="amwater-api",
    version="0.0.1",
    author="Jacob Schwartz",
    author_email="jake@schwartzpub.com",
    description="",
    zip_safe=False,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/schwartzpub/amwater_api",
    license="MIT",
    packages=setuptools.find_packages(
        'src',
        exclude=['__pycache__', 'venv']
    ),
    package_dir={'': 'src'},
    install_requires=[
        "httpx",
        "pydantic>=1.8.2,<1.10.0",
        "beautifulsoup4"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
