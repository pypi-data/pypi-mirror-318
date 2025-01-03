from setuptools import setup, find_packages

setup(
    name="uiaccessclient",
    version="0.9.0",
    description="UniFi Access API",
    keywords=["UniFi Access API"],
    install_requires=[
        "urllib3 >= 1.25.3, < 3.0.0",
        "python_dateutil >= 2.8.2",
        "pydantic >= 2",
        "typing-extensions >= 4.7.1",
    ],
    packages=find_packages(),
    include_package_data=True,
)
