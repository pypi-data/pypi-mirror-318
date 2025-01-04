from setuptools import setup, find_packages

NAME = "olab_prediction_market_sdk"
VERSION = "0.0.22"

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil", "olab_open_api==0.0.5", "hexbytes~=1.2.1", "web3~=7.6.1", "eth-account"]

setup(
    name=NAME,
    version=VERSION,
    description="OLAB Prediction Market Open API",
    author="nik.opinionlabs",
    author_email="nik@opinionlabs.xyz",
    url="",
    keywords=["PredictionMarket"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
)