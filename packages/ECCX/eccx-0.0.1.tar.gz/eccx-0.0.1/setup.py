from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required_packages = f.read().splitlines()

setup(
    name="ECCX",
    version="0.0.1",
    description="basic library i made in a day for elliptic curve cryptography and hybrid encryption. modeled after PGP.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="gamerjamer43",
    url="https://github.com/gamerjamer43/ECCX",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=required_packages,
    python_requires=">=3.6",
    include_package_data=True,
)