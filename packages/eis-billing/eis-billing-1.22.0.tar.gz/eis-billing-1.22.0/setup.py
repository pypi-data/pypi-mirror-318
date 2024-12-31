"""
    EMIL BillingService

    The EMIL BillingService API description  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: kontakt@emil.de
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "eis-billing"
VERSION = "1.22.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="EMIL BillingService",
    author="Contact us",
    author_email="kontakt@emil.de",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "EMIL BillingService"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    The EMIL BillingService API description  # noqa: E501
    """
)
