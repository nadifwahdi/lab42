from setuptools import find_packages, setup

setup(
    name="lab42",
    version="0.1.0",
    packages=find_packages(where="packages"),
    package_dir={"": "packages"},
    install_requires=[],
    python_requires=">=3.8",
)
